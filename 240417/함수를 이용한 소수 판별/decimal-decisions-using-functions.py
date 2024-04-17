a, b = tuple(map(int,input().split()))

def padd(num1, num2):
    addNum = 0
    for i in range(num1, num2+1):
        for j in range(2,i):
            if i%j==0:
                break
            if j==i-1:
                addNum+=i
        if i==2:
            addNum+=2
    return addNum


print(padd(a,b))