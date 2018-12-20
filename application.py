from flask import Flask,render_template,request
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    now=datetime.date.today()
    new_year= now.month==1 and now.day==1
    delta=datetime.date(now.year+1,1,1)-now
    return render_template("newyear.html",new_year=new_year,days=delta.days)

@app.route("/sajan")
def hello_1(name=' sajan'):
    return render_template("index.html",name=name)

@app.route("/lists")
def listing():
    listing=['a','b','c','d','e']
    return render_template("list.html",listing=listing)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/hello",methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/more")
def more():
    return render_template("more.html")
