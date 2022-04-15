#!/usr/bin/python3

# project: https://github.com/csfeeser/Python/blob/master/TLG/flask_project.md

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

questions = [{
    "question" : "The Eagle 5 just got away! What speed should you use to catch them?",
    "gif" : "https://cdn-images-1.medium.com/max/1600/0*arSYWialtHhdLo6h.gif",
    "correct_answer" : "Ludicrous speed",
    "incorrect_answers" : ["Regular speed", "Light speed", "Ridiculous speed" ],
    "all_answers" : ["Regular speed", "Light speed", "Ridiculous speed", "Ludicrous speed"]
}]


@app.route("/spaceballs-api")
def getapi():
    return jsonify(questions)

@app.route("/")
def index():
    question = questions[0]["question"]
    answers = questions[0]["all_answers"]
    return render_template("questpost.html", quest = question, answs = answers)

@app.route("/question", methods = ["POST"])
def question():
    getans = request.form.get("ans").capitalize()
    if getans in questions[0]["all_answers"]:        
        return redirect(url_for("getresult", answer = getans))
    else:
        return redirect("/") 

@app.route("/getresult/<answer>")
def getresult(answer):
    correct_answer = questions[0]["correct_answer"]
    return render_template("result.html", result = answer,  corrans = correct_answer)

@app.route("/end", methods = ["POST"])
def end():
    getans = request.form.get("go").lower()
    if getans == "go!":
        return redirect(url_for("finale"))
    else:
        return redirect(url_for("getresult", answer = "ludicrous speed"))

@app.route("/finale")
def finale():
    return render_template("finale.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)