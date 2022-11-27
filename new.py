#calculater
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)
 
def div(a,b):
    print(a/b)
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=str(input("operator:"))

if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="/":
    div(a,b)
elif c=="*":
    mul(a,b)