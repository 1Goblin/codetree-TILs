n = int(input())
arr = list(map(int, input().split()))

fm = arr[0]
tm = arr[0]

for i in arr:
    if i>fm:
        fm = i 
    elif i>tm:
        tm = i
print(fm, tm)