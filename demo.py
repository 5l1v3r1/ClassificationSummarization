# -*- coding: utf-8 -*-
from article import Article



#import urllib

#items = microdata.get_items(urllib.urlopen(url))
#item = items[0]
#item.itemtype

#item.name

#item.colleagues


#print(item.articleBody.strip())
#print(item.alternativeHeadline.strip())
#print item.json()


#a = Article(url)


#url = "http://www.haberturk.com/ekonomi/is-yasam/haber/1339299-gumruk-birligi-anlasmasi-guncelleniyor"
url='http://www.ensonhaber.com/cumhuriyetin-yayinladigi-referandum-anketi-2017-03-11.html'
#url = "http://edition.cnn.com/2017/03/11/asia/south-korea-park-geun-hye-protests/index.html"

article1 = Article()
article1.download(url)
article1.set_category()
print(article1.displayUrl())
print(article1.get_title())
#print(article1.get_text())
print(article1.get_thumbnailUrl())
print(article1.get_summary())
print(article1.get_category())
print(article1.get_json())
#print(article1.update_solr())
#print(article1.displayJson())
