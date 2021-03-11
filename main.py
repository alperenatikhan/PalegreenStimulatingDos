from flask import Flask,request,redirect, url_for, render_template
import sqlite3


app = Flask('app')

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        keyword = request.form["keyword"]
        return redirect(url_for("results",keyword = keyword))
    else:
        return render_template("base.html")

@app.route("/<keyword>", methods=["POST", "GET"])
def results(keyword):
    con = sqlite3.connect("russia_articles.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    search_str = "select * from russia_articles WHERE field2 like '%search%' or field4 like '%search%'"
    search_str= str(search_str).replace("search", str(keyword))
    cur.execute(search_str)
    rows = cur.fetchall()
    number_articles = len(rows)
    if request.method == "POST":
        keyword = request.form["keyword"]
        return redirect(url_for("results",keyword = keyword))
    return render_template("results.html", rows = rows, number_articles= number_articles)

app.run(host='0.0.0.0', port=8000)