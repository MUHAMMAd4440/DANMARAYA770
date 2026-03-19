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
