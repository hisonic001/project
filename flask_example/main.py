from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("html.html")

@app.route("/contact")
def contact():
  return "Contact Me Plz!!"

@app.route("/<username>")
def welcome(username):
  return f'Welcome {username}, This is Flask Webpage'



app.run(host="0.0.0.0")

