a, b = map(int, input().split())
cnt = 0

def ch(num):
    s = 0
    for i in range(2,num):
        if num%i==0:
            return False
    while (num>=1):
        s += num%10
        num = num//10
    if s%2!=0:
        return False
    return True

for i in range(a,b+1):
    if ch(i):
        cnt+=1

print(cnt)