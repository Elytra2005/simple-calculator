# simple calculator project

def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b
    
def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
    
numberOne = int(input("Number: "))
symbol = input("Symbol: ")
numberTwo = int(input("Number: "))

while True:
    if(symbol == "+"):
        print(add(numberOne, numberTwo))
    elif(symbol == "-"):
        print(subtract(numberOne, numberTwo))
    elif(symbol == "*"):
        print(multiply(numberOne, numberTwo))
    elif(symbol == "/"):
        printf(divide(numberOne, numberTwo))
    else:
        print("Error")
        break


    
    
    
    
