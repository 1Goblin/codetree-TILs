a, b = tuple(map(int ,input().split()))

cnt = 0

def check369(num):
    if (num//10)%3==0 or (num%10)%3==0:
        return True

def mul3(num):
    if num%3==0:
        return True


for i in range(a,b+1):
    if check369(i) or mul3(i):
        cnt+=1


print(cnt)