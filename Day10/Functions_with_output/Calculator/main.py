# Calculator
from art import logo
# Sum

def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiplication
def mul(n1, n2):
    return n1 * n2

# Division

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number:  "))

    for operator in operations:
        print(operator)
    conitnue_calculation = True
    while conitnue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number:  "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n ' to start a new calculation: ") == "y":
            num1 = answer
        else:
            conitnue_calculation = False
            calculator()
        
calculator()
    # operation_symbol = input("Pick an operation: ") 
    # num3 = int(input("What's the next number?: "))
    # calculation_function = operations[operation_symbol]
    # # second_answer = calculation_function(calculation_function(num1, num2), num3)
    # second_answer = calculation_function(first_answer, num3)
    # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    # result = input("If you want to continue using the output type 'y' else type 'n' to exit")
    # if result == "n":
    #     conitnue_calculation == False
        
    
