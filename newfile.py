print("Welcome to simple calculator")
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
a=float(input("Enter the 1st value:"))
b=float(input("Enter the 2nd value:"))
print("Select operation")
choice=input("1.Addition,2.subtraction,3.multiplication,4.division,\nEnter the operation no:")
if(choice == '1'):
    print("Addition(a+b):",(a+b))
    add(a,b)
elif(choice == '2'):
    print("Subtraction(a-b):",(a-b))
    sub(a,b)
elif(choice == '3'):
    print("Multiplication(a*b):",(a*b))
    mul(a,b)
elif(choice == '4'):
    print("Division(a/b):",(a/b))
    div(a,b)
else:
    print("invalid operation")