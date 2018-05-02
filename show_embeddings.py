
import yaml
from repository.mongo_ops import iterate_mod_questions_in_mongo

from bd_gensim.gram_facade import GramFacade
from bd_gensim.doc2vec_facade import Doc2VecFacade

if __name__ == '__main__':

    config = yaml.safe_load(open("config.yml"))
    data_dir = config['data_dir']
    models_dir = config['models_dir']


    doc2vecFacade = Doc2VecFacade(models_dir)
    doc2vecFacade.load_models()
