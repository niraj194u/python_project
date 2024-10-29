from flask import Flask, request

app = Flask(__name__)

@app.route("/calculate")
def calculate():
    # Get parameters from URL
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        operation = request.args.get("operation")

        # Perform the calculation
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

if __name__ == "__main__":
    app.run(debug=True)
