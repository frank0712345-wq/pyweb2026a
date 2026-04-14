import random
from flask import Flask, render_template, request
from datetime import datetime
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from firestore.read3 import search_teacher

# ===== Firebase 初始化 =====
if not firebase_admin._apps:

    if os.path.exists("serviceAccountKey.json"):
        cred = credentials.Certificate("serviceAccountKey.json")

    else:
        firebase_config = os.getenv("FIREBASE_CONFIG")
        cred = credentials.Certificate(json.loads(firebase_config))

    firebase_admin.initialize_app(cred)

db = firestore.client()

# ===== 這個一定要存在 =====
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

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入游禎友的網站首頁</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>今天日期</a><hr>"
    link += "<a href=/about>關於禎友</a><hr>"
    link += "<a href=/welcome?u=禎友&dep=靜宜資管>GET傳值</a><hr>"   
    link += "<a href=/account>POST傳值(帳號密碼)</a><hr>" 
    link += "<a href=/math>數學運算</a><hr>"
    link += "<a href=/cup>擲茭</a><hr>"
    link += "<a href=/teacher>讀取Firestore資料(教師查詢)</a><hr>"
    return link

@app.route("/teacher", methods=["GET", "POST"])
def teacher():
    results = []
    keyword = ""

    if request.method == "POST":
        keyword = request.form["keyword"]
        results = search_teacher(keyword)

    return render_template("teacher.html", results=results, keyword=keyword)

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>回到網站首頁</a>"

@app.route("/today")
def today():
    now = datetime.now()
    year  = str(now.year)
    month = str(now.month)
    day   = str(now.day)
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime=now)

@app.route("/about")
def about():
    return render_template("mis2a.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    x = request.values.get("u")
    y = request.values.get("dep")
    return render_template("welcome.html", name=x, dep=y)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/math", methods=["GET", "POST"])
def math():
    if request.method == "POST":
        x = int(request.form["x"])
        opt = request.form["opt"]
        y = int(request.form["y"])      
        result = "您輸入的是：" + str(x) + opt + str(y)
        
        if (opt == "/" and y == 0):
            result += "，除數不能為0"
        else:
            match opt:
                case "+":
                    r = x + y
                case "-":
                    r = x - y
                case "*":
                    r = x * y
                case "/":
                    r = x / y
                case _:
                    return "未知運算符號"
            result += "=" + str(r) + "<br><a href=/>返回首頁</a>"          
        return result
    else:
        return render_template("math.html")

@app.route('/cup', methods=["GET"])
def cup():
    action = request.values.get("action")
    result = None

    if action == 'toss':
        x1 = random.randint(0, 1)
        x2 = random.randint(0, 1)
        
        if x1 != x2:
            msg = "聖筊：表示神明允許、同意，或行事會順利。"
        elif x1 == 0:
            msg = "笑筊：表示神明一笑、不解，或者考慮中，行事狀況不明。"
        else:
            msg = "陰筊：表示神明否定、憤怒，或者不宜行事。"
            
        result = {
            "cup1": "/static/" + str(x1) + ".jpg",
            "cup2": "/static/" + str(x2) + ".jpg",
            "message": msg
        }
        
    return render_template('cup.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)