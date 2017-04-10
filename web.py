from flask import Flask, render_template, request
from article import Article
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        Url = request.form['Url']
        article = Article()
        article.download(Url)
        article.set_summary()
        article.set_category()
        print(article.get_thumbnailUrl())

        result = {'title': article.get_title(),
                  'text': article.get_text(),
                  'category': article.get_category(),
                  'thumbnail': article.get_thumbnailUrl(),
                  'summary': article.get_summary()
                  }
        return render_template("result.html",result = result)


if __name__ == '__main__':
   app.run(debug = True)