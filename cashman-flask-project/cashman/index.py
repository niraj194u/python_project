from flask import Flask

app = Flask(__name__)

# Define the /hello_world route
@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)