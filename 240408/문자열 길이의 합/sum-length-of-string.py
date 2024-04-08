n = int(input())
arr=[]
cnt=0
c = 0
for i in range(n):
    a = input()
    arr.append(a)
    if a[0]=="a":
        cnt+=1
    c+=len(a)

print(c, cnt)