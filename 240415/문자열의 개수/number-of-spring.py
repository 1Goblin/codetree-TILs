p = 0
a = []
while(1):
    n = input()
    if n=="0":
        break
    p+=1
    if p%2==1:
        a+=[n]
print(p)

for i in a:
    print(i)