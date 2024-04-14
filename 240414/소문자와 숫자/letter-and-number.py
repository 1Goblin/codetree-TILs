n = input()

for i in n:
    if i>="A" and i<="Z":
        print(i.lower(),end="")
    elif i>="0" and i<="9":
        print(i,end="")
    elif i>="a" and i<="z":
        print(i,end="")
    else:
        continue