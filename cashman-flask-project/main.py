from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/get-user/<user_id>",methods=["GET"])

def get_user(user_id):
    user_data ={
        "user_data": user_id,
        "name": "niraj raj",
        "email": "niraj994u@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"]=extra

    return jsonify(user_data),200

if __name__ == "__main__":
    app.run(debug=True)    