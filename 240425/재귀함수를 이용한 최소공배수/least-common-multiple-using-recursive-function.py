n = int(input())
arr = list(map(int, input().split()))

def mul(a,b):

    min_num = min(a, b)
    max_num = max(a, b)

    current_num = max_num
    while True:
        if current_num % min_num == 0:
            return current_num
        current_num += max_num
    

def func(arr, n):

    if n==0:
        return arr[0]

    return mul(func(arr, n-1), arr[n])

      
print(func(arr, n-1))