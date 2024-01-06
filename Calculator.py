
def calculator(a, b, operation):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    else:
        result = None
        print("Wrong Syntax!")
    return result
print("WELCOME, THIS IS A CALCULATOR.")

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
operation = input("Enter the operation symbol (+,-,*,/): ")

result = calculator(a, b, operation)
if result is not None:
    print(a, operation, b, "=", result)
