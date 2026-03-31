import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "游禎友",
  "mail": "frank0712345@gmail.com",
  "lab": 579
}

doc_ref = db.collection("靜宜資管").document("Yu Chen Yu")
doc_ref.set(doc)