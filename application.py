from flask import Flask,render_template
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    now=datetime.date.today()
    new_year= now.month==1 and now.day==1
    delta=datetime.date(now.year+1,1,1)-now
    return render_template("newyear.html",new_year=new_year,days=delta.days)

@app.route("/sajan")
def hello(name=' sajan'):
    return render_template("index.html",name=name)

@app.route("/lists")
def listing():
    listing=['a','b','c','d','e']
    return render_template("list.html",listing=listing)

@app.route("/more")
def more():
    return render_template("more.html")
