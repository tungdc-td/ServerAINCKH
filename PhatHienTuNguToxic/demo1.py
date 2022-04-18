# -*- coding: utf-8 -*-
from PhatHienTuNguToxic.tokenization.crf_tokenizer import CrfTokenizer
from PhatHienTuNguToxic.word_embedding.word2vec_gensim import Word2Vec
from PhatHienTuNguToxic.text_classification.short_text_classifiers import BiDirectionalLSTMClassifier, load_synonym_dict

from flask import Flask 
from flask import jsonify
import json


word2vec_model = Word2Vec.load('PhatHienTuNguToxic/models/pretrained_word2vec.bin')



# Load model 
tokenizer = CrfTokenizer(config_root_path='PhatHienTuNguToxic/tokenization/',
                         model_path='PhatHienTuNguToxic/models/pretrained_tokenizer.crfsuite')
sym_dict = load_synonym_dict('PhatHienTuNguToxic/data/sentiment/synonym.txt')
keras_text_classifier = BiDirectionalLSTMClassifier(tokenizer=tokenizer, word2vec=word2vec_model.wv,
                                                    model_path='PhatHienTuNguToxic/models/sentiment_model.h5',
                                                    max_length=10, n_epochs=10,
                                                    sym_dict=sym_dict)
# test the model
label_dict = {0: 'false', 1: 'true'}
def detection(text):
    try:
        test_sentences = [text]
        labels = keras_text_classifier.classify(test_sentences, label_dict=None)

        _json = {'toxic': str(labels[0])}
       
        r = json.dumps(_json)
        
        return r
    except Exception as e:
        return "error"
        print(e)
        

#test_sentences = ['alo', 'khai giang mua', 'khai giang mua vcl', 'dit cu may']
#labels = keras_text_classifier.classify(test_sentences, label_dict=None)
#print(labels)  
