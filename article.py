# -*- coding: utf-8 -*-

from gensim.summarization import summarize
import microdata
import urllib.request
from mysolr import Solr
import requests
from category import Category
import pysolr


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

    def set_summary(self, text):
        summary = summarize(text, ratio=0.5)
        self.summary = summary

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


    def update_solr(self):
        solr = pysolr.Solr('http://localhost:8983/solr/article', timeout=10)
        solr.add(self.get_json())

    def get_text(self):
        return self.text

    def get_title(self):
        return self.title

    def get_thumbnailUrl(self):
        return self.thumbnailUrl
