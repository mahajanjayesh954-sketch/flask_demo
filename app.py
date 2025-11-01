#flask app routing

from flask import Flask


#simple flask app
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
 return"<h1>welcome to flask app</h1>"

@app.route("/index",methods=["GET"])
def index():
   return "<h2>about page</h2>"
#variable rules
@app.route("/success/<score>")
def success(score):
    return "the person has passed with score:"+score
@app.route()

if __name__=="__main__":
    app.run(debug=True)