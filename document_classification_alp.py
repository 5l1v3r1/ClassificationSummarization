#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from sklearn.datasets import base

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import io
import numpy as np

"""
train datasını trainetme_traine dosya pathını veya ismini direk vererek category category datalarını okuyor



data = open("1.txt").read()

bu kodda ise deneme datasını yüklüyorsun
print(trainetme_train.target_names[gs_clf.predict([data])[0]])
bu kod ise categoryriyi print ettiriyor

"""
#categories = ['spor','teknoloji']
trainetme_train = base.load_files("news")


'''
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
 ])
'''
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)),
])
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
             'tfidf__use_idf': (True, False),
            'clf__alpha': (1e-2, 1e-3) }


gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)

gs_clf = gs_clf.fit(trainetme_train.data[:1000], trainetme_train.target[:1000])
data = open("1.txt").read()
#print(trainetme_train.target_names[gs_clf.predict([data])[0]])

print(trainetme_train.target_names[gs_clf.predict([data])])

predicted = text_clf.predict(trainetme_train)
sonuc=np.mean(predicted == data)
print(sonuc)

'''
with open("data.pkz", 'rb') as f:
    compressed_content = f.read()
file = open("deneme.txt","w")
file.write(compressed_content)
file.close()
'''