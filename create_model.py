import logging

import yaml
from repository.mongo_ops import iterate_mod_questions_in_mongo

from bd_gensim.gram_facade import GramFacade
from bd_gensim.doc2vec_facade import Doc2VecFacade

if __name__ == '__main__':

    config = yaml.safe_load(open("config.yml"))
    data_dir = config['data_dir']
    models_dir = config['models_dir']

    mongo_connection = config['mongo_connection']
    gramFacade = GramFacade(models_dir,10,10)
    all_questions = list(iterate_mod_questions_in_mongo(mongo_connection, separator=False))
    gramFacade.create_model(all_questions )

    bigrams = gramFacade.export_bigrams(all_questions )
    trigrams = gramFacade.export_trigrams(bigrams)
    with open(data_dir+"/bigrams.txt","w") as f:
        print(bigrams, file=f)
    with open(data_dir+"/trigrams.txt","w") as f:
        print(trigrams, file=f)

    doc2vecFacade = Doc2VecFacade(models_dir, window=7, min_count=3, sample=0.001, epochs=80, alpha=0.1, vector_size=400, batch_size=10000)
    doc2vecFacade.create_model(trigrams)
