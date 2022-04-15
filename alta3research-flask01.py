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
    "incorrect_answers" : ["Regular speed", "Light speed", "Ridiculous speed" ]
}]

question = questions[0]["question"]
correct_answer = questions[0]["correct_answer"]
incorrect_answers = questions[0]["incorrect_answers"]
answers = []
for inc_ans in incorrect_answers:            
    answers.append(inc_ans)
answers.append(correct_answer)

@app.route("/spaceballs-api")
def getapi():
    return jsonify(questions)

@app.route("/")
def index():
    return render_template("questpost.html", quest = question, answs = answers)

@app.route("/answer", methods = ["POST"])
def answer():
    getans = request.form.get("ans").capitalize()
    if getans in answers:        
        return redirect(url_for("result", answer = getans))
    else:
        return redirect("/") 

@app.route("/result/<answer>")
def result(answer):
    return render_template("result.html", result = answer,  corrans = correct_answer)

@app.route("/end", methods = ["POST"])
def end():
    getans = request.form.get("go").lower()
    if getans == "go!":
        return redirect(url_for("finale"))
    else:
        return redirect(url_for("result", answer = correct_answer))

@app.route("/finale")
def finale():
    return render_template("finale.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)