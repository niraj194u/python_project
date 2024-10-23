from flask import Flask

app = Flask(__name__)

# Define the /home route
@app.route('/home')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
