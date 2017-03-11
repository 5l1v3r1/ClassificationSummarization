import microdata
import urllib.request
class Article:
    'Common base class for all employees'
    articleCount = 0

    def __init__(self, url):
        self.url = url
        self.text = u''
        self.title = u''
        self.json={}
        Article.articleCount += 1

    def displayCount(self):
        print (Article.articleCount)

    def displayUrl(self):
        print ("Url : ", self.url)

    def displayJson(self):
        print (self.json)

    def download(self):
        items = microdata.get_items(urllib.request.urlopen(self.url))
        item = items[0]

        self.set_text(item.articleBody)
        self.set_title(item.alternativeHeadline)
        self.json = item.json()

    def set_text(self, text):
        self.text = text.strip()

    def get_text(self):
        print (self.text)

    def set_title(self, text):
        self.title = text.strip()

    def get_title(self):
        print (self.title)


