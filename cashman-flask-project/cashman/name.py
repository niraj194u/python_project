from flask import Flask

app = Flask(__name__)

@app.route("/submit/<name>/<email>", methods=["Get"])
def submit(name,email):
   
    return f"Submitted! Name: {name}, Email: {email}"

if __name__ == "__main__":
    app.run(debug=True)