arr = list(map(int, input().split()))
cnt = 0
s = 0
for i in arr:
    if i==0:
        break
    elif i%2==0:
        cnt+=1
        s+=i

print(f"{cnt} {s}")