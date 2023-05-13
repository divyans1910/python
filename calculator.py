
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Division
def divide(n1,n2):
    return n1/n2

#Dictionary
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }

def calculator():
    num1=int(input("Enter the first number: "))
    print("Which operation would you like to use: ")
    for op in operations:
        print(op)
    shdcontinue= True
    while shdcontinue:
        opt=input("-> ")
        num2=int(input("Enter the second number: "))
        calcfunc=operations[opt]
        answer= calcfunc(num1,num2)
        print(f"{num1} {opt} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or 'n' to start new calculation: ")=="y":
            num1=answer
        else:
            shdcontinue= False
            calculator()

calculator()

