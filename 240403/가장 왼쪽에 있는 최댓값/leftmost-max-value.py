import sys

n = int(input())
arr = list(map(int, input().split()))

max_value = -sys.maxsize
e =1
p = []

while(1):
    for i in range(n):
        if arr[i]>max_value:
            max_value = arr[i]
            m = i
        if i==(n-1):
            max_value = -sys.maxsize
            n = m
            p.append(m)
    if n==0:
        break

for k in p:
    print(k+1,end=" ")