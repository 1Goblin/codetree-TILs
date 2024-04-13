a = input()
b = input()

al = len(a)
bl = len(b)
c=0
while(c<10):
    for i in range(al):
        if a[i:i+bl] == b:
            a = a[0:i] + a[i+bl::]
            al = len(a)
            break;
    c+=1
    

print(a)