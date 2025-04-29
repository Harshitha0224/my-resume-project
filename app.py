from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f"<h1>Thank you, {name}!</h1><p>Your message: {message}</p>"

if __name__ == "__main__":
    app.run(debug=True)
