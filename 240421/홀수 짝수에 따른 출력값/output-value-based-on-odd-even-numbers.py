n = int(input())

def fun(num):
    if num == 2:
        return 2
    elif num == 1:
        return 1

    return fun(num-2) + num

print(fun(n))