n = int(input())
c=0
for i in range(n):
    arr = list(map(int, input().split()))
    s = 0
    cnt = 0
    for j in arr:
        s+=j
        cnt+=1
    if s/cnt>=60:
        print("pass")
        c+=1
    else:
        print("fail")
print(c)