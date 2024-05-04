import sys

a, b, c = tuple(map(int, input().split()))

max_num = -sys.maxsize

k = 0

an = c//a
bn = c//b
for i in range(an):
    for j in range(bn):
        num = (a*i) + (b*j)
        if num<=c:
            max_num = max(num,max_num)

print(max_num)