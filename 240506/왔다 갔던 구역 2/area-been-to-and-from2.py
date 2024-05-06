n = int(input())
OFFSET = 100

arr = [0] * 200

d = {
    "R" : 1,
    "L" : -1
}

c = 100

for _ in range(n):

    a, b = input().split()
    a = int(a)

    if d[b] == 1:
        for i in range(c,c+a*d[b],d[b]):
            arr[i]+=1
            c = i+1
    else:
        c -= 1
        for i in range(c,c+a*d[b],d[b]):
            arr[i]+=1
            c = i
    
cnt = 0

for i in arr:
    if i>=2:
        cnt+=1

print(cnt)