n = int(input())

def fibo(num):

    if num<=2:
        return 1

    return fibo(num-2) + fibo(num-1)

print(fibo(n))