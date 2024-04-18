a, b = map(int,input().split())

cnt = 0

def on(num):
    if num%2!=0 and num%10!=5 and (num%3!=0 or num%9==0):
        return True
    else:
        return False


for i in range(a,b+1):
    if on(i):
        cnt+=1

print(cnt)