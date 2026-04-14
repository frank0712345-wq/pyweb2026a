import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

if not firebase_admin._apps:

    if os.path.exists("serviceAccountKey.json"):
        cred = credentials.Certificate("serviceAccountKey.json")
    else:
        firebase_config = os.getenv("FIREBASE_CONFIG")
        cred = credentials.Certificate(json.loads(firebase_config))

    firebase_admin.initialize_app(cred)

db = firestore.client()

def search_teacher(keyword):
    collection_ref = db.collection("靜宜資管")
    docs = collection_ref.get()

    results = []

    for doc in docs:
        data = doc.to_dict()
        name = data.get("name", "")
        lab = data.get("lab", "")

        if keyword in name:
            results.append({
                "name": name,
                "lab": lab
            })

    return results

if __name__ == "__main__":
    keyword = input("請輸入關鍵字：")
    print(search_teacher(keyword))