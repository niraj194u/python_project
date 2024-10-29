from flask import Flask, request

app = Flask(__name__)

# Route using query parameters
@app.route("/calculate")
def calculate():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        operation = request.args.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Error: Division by zero is not allowed"
            result = num1 / num2
        else:
            return "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."

        return f"The result is: {result}"
    except (TypeError, ValueError):
        return "Error: Please provide valid numbers and an operation."

# Route using path parameters
@app.route("/calculate/<float:num1>/<float:num2>/<operation>")
def calculate_with_path(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        result = num1 / num2
    else:
        return "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."

    return f"The result is: {result}"

if __name__ == "__main__":
    app.run(debug=True)
