from flask import Flask, render_template, request

app = Flask(__name__)


answers = {
    "q1": "b",
    "q2": "b",
    "q3": "b",
    "q4": "a",
    "q5": "b",
    "q6": "a",
    "q7": "b",
    "q8": "b",
    "q9": "b",
    "q10": "c",
    "q11": "a",
    "q12": "c",
    "q13": "b",
    "q14": "a",
    "q15": "c",
    "q16": "b",
    "q17": "c",
    "q18": "b",
    "q19": "b",
    "q20": "a"
}


@app.route("/")
def home():
    return render_template("main.html")



def submit_quiz():
    score = 0

    for  question, correct_answer in answers.items():
        user_answer = request.form.get(question)

        if user_answer == correct_answer:
            score += 1

    return render_template(
        "result.html",
        score=score,
        total=len(answers)
    )


if __name__ == "__main__":
    app.run(debug=True)
