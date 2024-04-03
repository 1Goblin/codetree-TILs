import sys

arr = list(map(int, input().split()))

max_val = -sys.maxsize

for i in arr:
    if i>max_val:
        max_val=i

print(max_val)