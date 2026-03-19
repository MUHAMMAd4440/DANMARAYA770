from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DANMARAYA CBT System"

if __name__ == '__main__':
    app.run(debug=True)
# CBT project by Bashir
print("App started")
return "Welcome to DANMARAYA CBT System"
return "Welcome to DANMARAYA CBT System - Start Exam"
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What is 2 + 2?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "Capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Ibadan"], "answer": "Abuja"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i in range(len(questions)):
            if request.form.get(f"q{i}") == questions[i]["answer"]:
                score += 1
        return render_template("result.html", score=score, total=len(questions))

    return render_template("quiz.html", questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
templates/index.html
<h1>DANMARAYA CBT SYSTEM</h1>
<a href="/quiz">Start Test</a>
templates/quiz.html
