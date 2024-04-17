a, b = tuple(map(int ,input().split()))

cnt = 0

def check369(num):
    num = list(str(num))
    for i in num:
        if i=="3" or i=="6" or i=="9":
            return True



def mul3(num):
    if num%3==0:
        return True


for i in range(a,b+1):
    if check369(i) or mul3(i):
        cnt+=1


print(cnt)