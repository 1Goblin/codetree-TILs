import sys

n = int(input())
arr = list(map(int, input().split()))


fm = -sys.maxsize
tm = -sys.maxsize

for i in arr:
    if i>fm:
        fm = i 
for k in arr:
    if fm>k and k>=tm:
        tm = k

print(fm, tm)