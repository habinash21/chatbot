# calculator_tool.py

def calculate(expression: str) -> str:
    """
    A simple calculator tool that handles:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulus

    Input examples:
        - "12 times 7"
        - "Add 45 and 30"
        - "50 minus 20"
        - "100 divided by 4"
        - "10 modulus 3"
    """
    expression = expression.lower().strip()

    try:
        # Addition
        if "add" in expression or "+" in expression or "plus" in expression:
            numbers = [int(s) for s in expression.replace("+", " ").split() if s.isdigit()]
            return str(sum(numbers))

        # Subtraction
        elif "minus" in expression or "-" in expression or "subtract" in expression:
            numbers = [int(s) for s in expression.replace("-", " ").split() if s.isdigit()]
            if len(numbers) >= 2:
                result = numbers[0]
                for n in numbers[1:]:
                    result -= n
                return str(result)
            return "❌ Need at least two numbers for subtraction."

        # Multiplication
        elif "times" in expression or "multiply" in expression or "x" in expression or "*" in expression:
            numbers = [int(s) for s in expression.replace("*", " ").replace("x", " ").split() if s.isdigit()]
            result = 1
            for n in numbers:
                result *= n
            return str(result)

        # Division
        elif "divide" in expression or "/" in expression:
            numbers = [int(s) for s in expression.replace("/", " ").split() if s.isdigit()]
            if len(numbers) == 2:
                if numbers[1] == 0:
                    return "❌ Division by zero is not allowed."
                return str(numbers[0] / numbers[1])
            return "❌ Division requires exactly two numbers."

        # Modulus
        elif "modulus" in expression or "mod" in expression or "%" in expression:
            numbers = [int(s) for s in expression.replace("%", " ").split() if s.isdigit()]
            if len(numbers) == 2:
                if numbers[1] == 0:
                    return "❌ Modulus by zero is not allowed."
                return str(numbers[0] % numbers[1])
            return "❌ Modulus requires exactly two numbers."

        else:
            return "❌ Unsupported operation. Only +, -, *, /, % are supported."

    except Exception as e:
        return f"❌ Error: {e}"
