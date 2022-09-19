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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbols in operations:
        print(symbols)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats's the next number?: "))
        answer = operations[operation_symbol](num1,num2) # call the function add/subtract/divide/multiply based on the key/value fro the dictionary

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a neu calculation or type 'e' to exit.: ")
        
        if cont == "y":
            num1 = answer
        elif cont == "n":
            should_continue = False
            calculator() #recursion to start a new calculation
        else:
            return

calculator()

