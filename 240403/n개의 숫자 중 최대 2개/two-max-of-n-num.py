import sys

n = int(input())
arr = list(map(int, input().split()))

fm = arr[0]
tm = arr[0]

for i in arr:

    if i<=fm and i>tm:
        tm = i

    if i>fm:
        fm = i
    
print(fm, tm)