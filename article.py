# -*- coding: utf-8 -*-

from gensim.summarization import summarize
import microdata
import urllib.request
from mysolr import Solr
import requests
from category import Category
import pysolr
import nlp


class ArticleException(Exception):
    pass

class Article:
    'Common base class for all employees'
    articleCount = 0

    def __init__(self):
        self.url = u''
        self.text = u''
        self.title = u''
        self.summary = u''
        self.category = u''
        self.articleJson = {}


        self.thumbnailUrl = u''
        self.json = {}

        Article.articleCount += 1

    def displayCount(self):
        return Article.articleCount

    def displayUrl(self):
        return self.url

    def displayJson(self):
        return self.json

    def download(self,url):
        self.url = url
        items = microdata.get_items(urllib.request.urlopen(self.url))
        item = items[0]
        self.set_text(item.articleBody)
        self.set_title(item.alternativeHeadline)
        self.set_thumbnailUrl(item.thumbnailUrl)
        self.set_summary(item.articleBody)
        self.json = item.json()

    def set_text(self, text):
        self.text = text.strip()

    def set_title(self, text):
        self.title = text

    def set_summary(self, summary):
        """Summary here refers to a paragraph of text from the
        title text and body text
        """
        self.summary = summary[:5000]

    def set_summary2(self, text):
        summary = summarize(text, ratio=0.5)
        self.summary = summary

    def set_keywords(self, keywords):
        """Keys are stored in list format
        """
        if not isinstance(keywords, list):
            raise Exception("Keyword input must be list!")
        if keywords:
            self.keywords = keywords[:10]

    def nlp(self):
        text_keyws = list(nlp.keywords(self.text).keys())
        title_keyws = list(nlp.keywords(self.title).keys())
        keyws = list(set(title_keyws + text_keyws))
        self.set_keywords(keyws)

        max_sents = 5

        summary_sents = nlp.summarize(title=self.title, text=self.text, max_sents=max_sents)
        summary = '\n'.join(summary_sents)
        self.set_summary(summary)


    def set_category(self):
        cat = Category(self.text)
        self.category = cat.get_category()

    def get_category(self):
        return self.category


    def set_thumbnailUrl(self, url):
        self.thumbnailUrl = url

    def get_summary(self):
        return self.summary

    def get_json(self):
        document = [{
                'url': self.url,
                'category': self.get_category(),
                'image': self.get_thumbnailUrl(),
                'title': self.get_title(),
                'text':self.get_text(),
                'summary':self.get_summary()
            }]

        return document


    def get_text(self):
        return self.text

    def get_title(self):
        return self.title

    def get_thumbnailUrl(self):
        return self.thumbnailUrl


class Articles:
    def __init__(self):
        self.solr = pysolr.Solr('http://localhost:8983/solr/article', timeout=10)
        self.adricle=[]
    def add_adricle(self,url):
        article = Article()
        article.download(url)
        article.set_category()
        self.update_solr(article.get_json())
        return article.get_json()

    def update_solr(self,json):
        self.solr.add(json)

    def search(self,str):
        results = self.solr.search(str)
        return results

