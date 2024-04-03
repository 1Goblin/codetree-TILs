import sys

n = int(input())
arr = list(map(int, input().split()))


fm = -sys.maxsize
tm = -sys.maxsize

for i in arr:
    if i>fm:
        fm = i 
    elif i>tm:
        tm = i
print(fm, tm)