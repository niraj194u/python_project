from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

if __name__ == '__main__':
    app.run(debug=True)
