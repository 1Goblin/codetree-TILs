a1, b1, a2, b2 = tuple(map(int, input().split()))
x1, y1, x2, y2 = tuple(map(int, input().split()))


def cal(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)


if x1>a1:
    if y1>b1:
        print(cal(a1,x2,b1,y2))
    else:
        print(cal(a1,x2,y1,b2))
else:
    if y1>b1:
        print(cal(x1,a2,b1,y2))
    else:
        print(cal(x1,a2,y1,b2))