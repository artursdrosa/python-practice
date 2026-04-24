from operations import sum, sub, mult, div

try:
    num1 = float(input("Enter the first number: "))
    operacao = input("Choose the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operacao == "+":
        resultado = sum(num1, num2)
    elif operacao == "-":
        resultado = sub(num1, num2)
    elif operacao == "*":
        resultado = mult(num1, num2)
    elif operacao == "/":
        resultado = div(num1, num2)
    else:
        print("Invalid operation!")
        exit()

    print(f"Result: {resultado}")

except ValueError:
    print("Error: Invalid input. Please enter only numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
