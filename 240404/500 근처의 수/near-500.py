import sys
arr = list(map(int, input().split()))

a = -sys.maxsize
b = sys.maxsize

for i in arr:
    if i<500:
        if i>a:
            a=i
    elif i>500:
        if i<b:
            b=i
print(a, b)