
import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/article', timeout=10)

# How you'd index data.
'''solr.add([
    {
        "id": "doc_3",
        "title": "A test document",
    },
    {
        "id": "doc_4",
        "title": "The Banana: Tasty or Dangerous?",
    },
])'''

solr.delete(id='doc_1')
solr.delete(id='doc_2')
solr.delete(id='doc_3')
solr.delete(id='doc_4')
