import sys

a, b, c = tuple(map(int, input().split()))

max_num = -sys.maxsize

k = 0

an = c//a
bn = c//b
for i in range(an+1):
    for j in range(bn+1):
        num = (a*i) + (b*j)
        if num<=c:
            max_num = max(num,max_num)

print(max_num)