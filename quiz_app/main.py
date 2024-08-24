from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Simple quiz data with multiple choices
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Tolkien"], "answer": "Shakespeare"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
]

@app.get("/", response_class=HTMLResponse)
async def quiz_form():
    html_content = """
    <html>
        <head>
            <title>Simple Quiz</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .quiz-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    max-width: 400px;
                    width: 100%;
                }
                h1 {
                    font-size: 24px;
                    margin-bottom: 20px;
                    text-align: center;
                    color: #333;
                }
                p {
                    font-size: 18px;
                    margin-bottom: 10px;
                    color: #555;
                }
                input[type="radio"] {
                    margin-right: 10px;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="quiz-container">
                <h1>Simple Quiz</h1>
                <form action="/submit" method="post">
    """
    for i, q in enumerate(questions):
        html_content += f"<p>{q['question']}</p>"
        for j, option in enumerate(q['options']):
            html_content += f'<input type="radio" id="q{i}_option{j}" name="q{i}" value="{option}">'
            html_content += f'<label for="q{i}_option{j}">{option}</label><br>'

    html_content += """
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
    </html>
    """
    return html_content

@app.post("/submit", response_class=HTMLResponse)
async def quiz_submit(q0: str = Form(...), q1: str = Form(...), q2: str = Form(...)):
    answers = [q0, q1, q2]
    correct_answers = 0

    for i, q in enumerate(questions):
        if q['answer'].lower() == answers[i].strip().lower():
            correct_answers += 1

    html_content = f"""
    <html>
        <head>
            <title>Quiz Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .quiz-container {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    max-width: 400px;
                    width: 100%;
                    text-align: center;
                }}
                h1 {{
                    font-size: 24px;
                    margin-bottom: 20px;
                    color: #333;
                }}
                p {{
                    font-size: 18px;
                    margin-bottom: 10px;
                    color: #555;
                }}
                a {{
                    color: #007BFF;
                    text-decoration: none;
                    font-weight: bold;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="quiz-container">
                <h1>Quiz Results</h1>
                <p>You answered {correct_answers} out of {len(questions)} questions correctly.</p>
                <a href="/">Try Again</a>
            </div>
        </body>
    </html>
    """
    return html_content

