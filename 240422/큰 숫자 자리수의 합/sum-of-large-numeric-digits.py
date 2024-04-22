a, b, c = map(int, input().split())
num = a*b*c

def func(num):

    if num<10:
        return num
    

    return func(num//10) + num%10


print(func(num))