import os

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

calculator = {"+": add, "-": sub, "*": mul, "/": div}

def calculators():
    f_num = float(input("What is the first number?: "))

    cont = True

    while cont:
        for symbol in calculator:
            print(symbol)
        op = input("Pick an operation: ")
        s_num = float(input("What is the next number?: "))

        if op == "+":
            output = calculator["+"](f_num, s_num)
        elif op == "-":
            output = calculator["-"](f_num, s_num)
        elif op == "*":
            output = calculator["*"](f_num, s_num)
        elif op == "/":
            output = calculator["/"](f_num, s_num)

        print(f"{f_num} {op} {s_num} = {output}")

        next_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")

        if next_calc == "y":
            f_num = output
        elif next_calc == "n":
            os.system('clear')
            cont = False
            calculators()
            
calculators()
