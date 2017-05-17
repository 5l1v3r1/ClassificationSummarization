# *-* coding: utf-8 *-*
import json
import urllib.request
import jwt
__CORE_NAME__ = "article"

def get_result(search_term, category="*", page=0):
	search_term = search_term.replace(' ', "+")
	search_url = "http://localhost:8983/solr/{0}/select?q={1}&wt=json&indent=true".format(__CORE_NAME__, search_term)
	search_resp = urllib.request.urlopen(search_url)
	result = json.loads(search_resp.read())
	return result

result = get_result("borsa")


encoded=jwt.encode(result, 'secret', algorithm='HS256')
print(encoded)
decoded=jwt.decode(encoded, 'secret', algorithms=['HS256'])
print(decoded)
#print(json.dumps(result['response'], indent=4))