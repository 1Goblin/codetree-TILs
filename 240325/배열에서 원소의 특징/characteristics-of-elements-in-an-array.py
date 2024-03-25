arr = list(map(int, input().split()))
m = 0
for i in arr:
    if i%3==0:
        break
    m = i
print(m)