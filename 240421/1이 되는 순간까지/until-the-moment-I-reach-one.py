n = int(input())
cnt = 0

def func(num):

    global cnt

    if num==1:
        return 0
    
    if num%2==0:
        num = num//2
        cnt+=1
        return func(num)
    else:
        num = num//3
        cnt+=1
        return func(num)

func(n)

print(cnt)