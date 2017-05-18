from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pysolr
import json
import urllib.request
import urllib
import jwt


app = Flask(__name__)
api = Api(app)

__CORE_NAME__ = "article"



class Search(Resource):
    def get(self, str):

        search_term = str.replace(' ', "+")
        search_url = "http://localhost:8983/solr/{0}/select?q={1}&wt=json&indent=true".format(__CORE_NAME__,search_term)
        search_resp = urllib.request.urlopen(search_url)
        result = json.loads(search_resp.read())
        encoded = jwt.encode(result, 'secret', algorithm='HS256')
        return json.dumps(encoded.decode(encoding="utf-8"))


api.add_resource(Search, '/search/<str>')

if __name__ == '__main__':
    app.run(debug=True)