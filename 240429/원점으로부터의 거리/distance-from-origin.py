n = int(input())

class dot:
    def __init__(self, dis, num):
        self.dis = dis  
        self.num = num


dots = []

for i in range(1,n+1):
    x, y = map(int, input().split())
    if x>=0:
        if y>=0:
            dis = x+y
        else:
            dis = x-y
    else:
        if y>=0:
            dis = y-x
        else:
            dis = -x-y
        
    dots.append(dot(int(dis),i))


dots.sort(key = lambda x : (x.dis, x.num))

for i in dots:
    print(i.num)