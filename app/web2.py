from flask import Flask, render_template, request
import pysolr
import pysolr
import json
import urllib.request
import urllib
import jwt
from article import Article
app = Flask(__name__)
__CORE_NAME__ = 'article'
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        Url = request.form['Url']
        article = Article()
        article.addUrl(Url)
        #article.download(Url)
        #article.set_summary()
        #article.set_category()
        #article.add_solr()

        result = {'title': article.get_title(),
                  'text': article.get_text(),
                  'category': article.get_category(),
                  'thumbnail': article.get_thumbnailUrl(),
                  'summary': article.get_summary()
                  }
        return render_template("result.html",result = result)



@app.route('/searchresult',methods = ['POST', 'GET'])
def searchResult():
   if request.method == 'POST':
        Url = request.form['Url']
        search_term = Url.replace(' ', "+")
        search_url = "http://localhost:8983/solr/{0}/select?q={1}&wt=json&indent=true".format(__CORE_NAME__,search_term)
        search_resp = urllib.request.urlopen(search_url)
        result = json.loads(search_resp.read())
        result_response=result['response']['docs']
        print('print(result_response)')
        print(result_response)

        #encoded = jwt.encode(result, 'secret', algorithm='HS256')
        #return json.dumps(encoded.decode(encoding="utf-8"))
        #

        return render_template("searchresult.html",result = result_response)

if __name__ == '__main__':
   app.run(debug = True)