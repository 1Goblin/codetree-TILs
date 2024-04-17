a, b = tuple(map(int,input().split()))

def prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True 

for i in range(a, b+1):
    if prime(i):
        sump+=i

print(sump)