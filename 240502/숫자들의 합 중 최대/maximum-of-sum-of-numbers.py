import sys

x, y = tuple(map(int, input().split()))


def sn(num):

    if num<10:
        return num

    return sn(num//10) + num%10

max_c = -sys.maxsize

for i in range(x, y+1):

    max_c = max(sn(i),max_c)

print(max_c)