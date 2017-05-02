from flask import Flask, render_template, request, jsonify
from article import Article
import pysolr
import json
import urllib.request
import urllib
import jwt
import requests

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        Text = request.form['Text']
        article = Article()
        article.addText(Text)
        #article.download(Url)
        #article.set_summary()
        #article.set_category()
        #print(article.get_thumbnailUrl())

        result = {
                  'text': article.get_text(),
                  'category': article.get_category()
                  }
        return render_template("result3.html",result = result)

@app.route('/result2',methods = ['POST', 'GET'])
@app.route('/result2/<category>',defaults={'page': 1})
@app.route('/result2/<category>/<int:page>')
@app.route('/result2/<int:page>')
def result2(category=None,page=1):
   if request.method == 'POST':
       #__CORE_NAME__ = 'article'
       Url = request.form['Url']
       search_term = Url.replace(' ', "+")
       search_url = "http://localhost:8983/solr/haberler/select?facet.field=category&facet=on&indent=on&q={0}&rows=10&start=0&wt=json".format(search_term)
       r = requests.get(search_url)
       j_data = r.text
       b = json.loads(j_data)
       return render_template("searchresult2.html", cat=b['facet_counts']['facet_fields']['category'],
                               haber=b['response']['docs'])

   elif request.method == 'GET':
       sayfa=10*page
       search_url = "http://localhost:8983/solr/haberler/select?facet.field=category&facet=on&indent=on&q=*:*&rows=10&start={0}&wt=json".format(str(sayfa))
       if category !=None:
           search_url+='&fq=category:'+category
       r = requests.get(search_url)
       j_data = r.text
       b = json.loads(j_data)
       #search_resp = urllib.request.urlopen(search_url)
       #encoded = j_data.encode()
       #result = json.loads(search_resp.read().encode())
       #return render_template("result2.html",result =result['facet_counts']['facet_fields']['category'])
       if category is None:
            return render_template("searchresult3.html",cat =b['facet_counts']['facet_fields']['category'],haber=b['response']['docs'],page=page)
       else:
           return render_template("searchresult2.html", cat=b['facet_counts']['facet_fields']['category'],
                                  haber=b['response']['docs'], page=page, category=category)
       #return str(page)
@app.route('/search')
def search():
   return render_template('search.html')


@app.route('/searchresult',methods = ['POST', 'GET'])
def searchResult():
   if request.method == 'POST':
        Url = request.form['Url']
        __CORE_NAME__='article'
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
        #return result_response
        return render_template("searchresult.html",result = result_response)


@app.route('/searchresult2',methods = ['POST', 'GET'])
def searchResult2():
   if request.method == 'POST':
        Url = request.form['Url']
        __CORE_NAME__='article'
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
        #return result_response
        return render_template("searchresult2.html",result = result_response)

if __name__ == '__main__':
   app.run(debug = True)