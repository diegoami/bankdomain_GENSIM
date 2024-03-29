from gensim.models import Doc2Vec
from gensim import matutils


#

MODEL_FILENAME = 'doc2vec'

import numpy as np
from gensim.models.doc2vec import TaggedDocument
from datetime import timedelta
import logging


class LabeledLineSentence(object):
    def __init__(self, idxlist, texts):
        self.doc_list = idxlist
        self.texts = texts

    def __iter__(self):
        for idx, text in zip(self.doc_list, self.texts):
            wtok = text
            tags = [idx]

            yield TaggedDocument(words=wtok, tags=tags)


class Doc2VecFacade():

    def __init__(self, model_dir,  window=10, min_count=5, sample=0.001, epochs=30, alpha=0.1, vector_size=400, batch_size=10000, queue_factor=2, workers=8, version=1):

        self.model_dir = model_dir
        self.name="DOC2VEC-V"+str(version)

        self.window=window
        self.min_count=min_count
        self.sample = sample
        self.epochs = epochs
        self.alpha = alpha
        self.vector_size = vector_size
        self.batch_size = batch_size
        self.queue_factor = queue_factor
        self.workers = workers

    def load_models(self):
        model_filename = self.model_dir+'/'+MODEL_FILENAME
        self.model = Doc2Vec.load(model_filename)




    def create_model(self, texts):
        it = LabeledLineSentence(range(len(texts)), texts)
        logging.info("Creating model with {} texts".format(len(texts)))
        self.model = Doc2Vec(size=self.vector_size, window=self.window, workers=self.workers, alpha=self.alpha, min_alpha=0.0001,
                             epochs=self.epochs, min_count=self.min_count, sample=self.sample, batch_words=self.batch_size)  # use fixed learning rate
        self.model.build_vocab(it)

        logging.info("Starting to train......")

        self.model.train(it, total_examples=self.model.corpus_count, epochs=self.epochs, queue_factor=self.queue_factor)

        logging.info("Training completed, saving to  " + self.model_dir)
        self.model.save(self.model_dir + MODEL_FILENAME)

