a, b = map(int,input().split())

c = str(a+b)
 
d = 0

for i in c:
    if i=="1":
        d+=1


print(d)