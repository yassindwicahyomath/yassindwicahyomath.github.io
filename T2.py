def calculate(operator, num1, num2):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

result = calculate(operator, num1, num2)
print(result)
