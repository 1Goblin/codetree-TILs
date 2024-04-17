a, b, c =input().split()

a = int(a)
c = int(c)

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def div(a,b):
    return a//b

def mul(a,b):
    return a*b


if b=="+":
    print(f"{a} {b} {c} = {plus(a,c)}") 
elif b=="-":
    print(f"{a} {b} {c} = {minus(a,c)}")
elif b=="/":
    print(f"{a} {b} {c} = {div(a,c)}")
elif b=="*":
    print(f"{a} {b} {c} = {mul(a,c)}")
else:
    print("False")