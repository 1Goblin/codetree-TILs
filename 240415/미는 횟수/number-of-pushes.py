a = input()
b = input()

cnt = 0

for i in range(len(a)):
    a= a[-1] + a[:-1]
    cnt+=1
    if a==b:
        break

if cnt<len(a):
    print(cnt)
else:
    print("-1")