import firebase_admin
from firebase_admin import credentials, firestore
import os

# ===== Firebase 初始化（只在「單獨執行」時才做）=====
if not firebase_admin._apps:
    # 找到 serviceAccountKey.json（相對路徑）
    cred_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# 建立 Firestore client
db = firestore.client()


# ===== 查詢函式（給 Flask 用）=====
def search_teacher(keyword):
    collection_ref = db.collection("靜宜資管")
    docs = collection_ref.get()

    results = []
    for doc in docs:
        data = doc.to_dict()
        name = data.get("name", "")
        lab = data.get("lab", "")

        # 模糊查詢（包含關鍵字）
        if keyword in name:
            results.append({
                "name": name,
                "lab": lab
            })

    return results


# ===== CLI 模式（單獨執行）=====
if __name__ == "__main__":
    keyword = input("請輸入老師名字關鍵字：")
    results = search_teacher(keyword)

    if results:
        print("查詢結果：")
        for r in results:
            print(f"老師：{r['name']}，研究室：{r['lab']}")
    else:
        print("查無資料")