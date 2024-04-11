m = input()

e = 0
b = 0


for i in range(len(m)-1):
    if m[i]=="e" and m[i+1]=="e":
        e+=1

    if m[i]=="e" and m[i+1]=="b":
        b+=1
    
print(e, b)