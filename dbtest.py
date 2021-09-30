# from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
#
from google.cloud import firestore

# Add a new document
db = firestore.Client()
doc_ref = db.collection(u'test').document()

doc_ref.set({
    u'one': u'1 test',
    u'two': u'2',
    u'free': 3
})

# Then query for documents
test_ref = db.collection(u'test')

for doc in test_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))