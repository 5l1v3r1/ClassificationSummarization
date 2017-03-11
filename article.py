# -*- coding: utf-8 -*-
from gensim.summarization import summarize
import microdata
import urllib.request


class Article:
    'Common base class for all employees'
    articleCount = 0

    def __init__(self, url):
        self.url = url
        self.text = u''
        self.title = u''
        self.summary = u''
        self.thumbnailUrl = u''
        self.json = {}
        Article.articleCount += 1

    def displayCount(self):
        return Article.articleCount

    def displayUrl(self):
        return self.url

    def displayJson(self):
        return self.json

    def download(self):
        items = microdata.get_items(urllib.request.urlopen(self.url))
        item = items[0]
        self.set_text(item.articleBody)
        self.set_title(item.alternativeHeadline)
        self.set_thumbnailUrl(item.thumbnailUrl)
        self.json = item.json()

    def set_text(self, text):
        self.text = text.strip()

    def set_title(self, text):
        self.title = text.strip()

    def set_summary(self, text):
        summary = summarize(text, ratio=0.25)
        self.summary = summary

    def set_thumbnailUrl(self, url):
        self.thumbnailUrl = url

    def get_summary(self, summary):
        return self.summary

    def get_text(self):
        return self.text

    def get_title(self):
        return self.title

    def get_thumbnailUrl(self):
        return self.thumbnailUrl
