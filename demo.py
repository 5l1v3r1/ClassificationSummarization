
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


url = "http://www.ensonhaber.com/tuncay-ozkan-fetullah-gulen-senin-derini-yuzecegim-dedi-2017-03-11.html"
#url = "http://edition.cnn.com/2017/03/11/asia/south-korea-park-geun-hye-protests/index.html"

article1 = Article(url)
article1.download()
article1.displayUrl()
article1.get_title()
article1.get_text()
#article1.displayJson()
