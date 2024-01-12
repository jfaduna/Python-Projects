from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculate = operations[operation_symbol]
        result = calculate(first_number, second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {result}")

        option = input(f"Type 'y' to continue with {result}, or type 'n' to exit.")
        if option.lower() == 'y':
            first_number = result
        else:
            should_continue = False
            calculator()

calculator()
