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
    "correct_answer" : {"answer" :"Ludicrous speed", "gifs" : ["https://y.yarn.co/773c240a-5475-40f6-aa47-e7dc8766386d_text.gif#", "https://i.imgflip.com/fimzm.gif"]},
    "incorrect_answers" : {"answers" : ["Regular speed", "Light speed", "Ridiculous speed" ], "gif" : "https://th.bing.com/th/id/R.d4cea9a3e4acdc0759f0c3c15139114e?rik=%2bGQ59pUoS53HWQ&riu=http%3a%2f%2ffanfest.com%2fwp-content%2fuploads%2f2017%2f05%2fspaceballs-3.gif&ehk=qg%2f3JwlANXZmY%2f4qr4HsQ%2bIg14ASKv6g6EfAkQ6wKxU%3d&risl=&pid=ImgRaw&r=0"},
    "finale_gifs" : ["https://media.giphy.com/media/hgw9YM21ri61G/giphy.gif", "https://vignette3.wikia.nocookie.net/steven-universe/images/6/61/Gone-plaid-o.gif/revision/latest?cb=20150812153100"]
}]

correct_answer = questions[0]["correct_answer"]["answer"]
incorrect_answers = questions[0]["incorrect_answers"]["answers"]
answers = []
for inc_ans in incorrect_answers:            
    answers.append(inc_ans)
answers.append(correct_answer)

@app.route("/spaceballs-api")
def getapi():
    return jsonify(questions)

@app.route("/")
def index():
    question = questions[0]["question"]    
    gif = questions[0]["gif"]
    return render_template("questpost.html", quest = question, answs = answers, gif = gif)

@app.route("/answer", methods = ["POST"])
def answer():
    getans = request.form.get("ans").capitalize()
    if getans in answers:        
        return redirect(url_for("result", answer = getans))
    else:
        return redirect("/") 

@app.route("/result/<answer>")
def result(answer):    
    inc_gif = questions[0]["incorrect_answers"]["gif"]
    corr_dict = questions[0]["correct_answer"]
    return render_template("result.html", result = answer, corrdict = corr_dict, incgif = inc_gif)

@app.route("/end", methods = ["POST"])
def end():
    getans = request.form.get("go").lower()
    if getans == "go!":
        return redirect(url_for("finale"))
    else:
        return redirect(url_for("result", answer = correct_answer))

@app.route("/finale")
def finale():
    finale_gifs = questions[0]["finale_gifs"]
    return render_template("finale.html", gifs = finale_gifs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)