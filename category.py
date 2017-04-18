from sklearn.datasets import base
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
'''
categories = ['dunya', 'ekonomi', 'kultur-sanat', 'magazin', 'planet1', 'saglik', 'siyaset', 'spor', 'teknoloji',
              'turkiye', 'yasam']
news_train = base.load_files("news")
data = open("1.txt").read()
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)),
                     ])
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3)}
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(news_train.data[:1000], news_train.target[:1000])

print(news_train.target_names[gs_clf.predict([data])[0]])

'''
class Category:
    def __init__(self,text):
        self.data = text
        self.categories = []
        self.category=''
        self.set_category()

    def set_category(self):
        news_train = base.load_files("news")

        self.categories = ['dunya', 'ekonomi', 'kultur-sanat', 'magazin', 'saglik', 'siyaset', 'spor',
                           'teknoloji', 'turkiye', 'yasam']

        text_clf = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                   alpha=1e-3, n_iter=5, random_state=42)),
                             ])
        parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                      'tfidf__use_idf': (True, False),
                      'clf__alpha': (1e-2, 1e-3)}

        gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
        gs_clf = gs_clf.fit(news_train.data[:1000], news_train.target[:1000])

        self.category=news_train.target_names[gs_clf.predict([self.data])[0]]

    def get_category(self):
        return self.category

#data = open("1.txt").read()
#cat = Category(data)
#print(cat.get_category())