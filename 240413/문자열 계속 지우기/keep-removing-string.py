a = input()
b = input()

al = len(a)
bl = len(b)
c=al
d=0
while(d<c):
    for i in range(al):
        if a[i:i+bl] == b:
            a = a[0:i] + a[i+bl::]
            al = len(a)
            break;
    d+=1
    

print(a)