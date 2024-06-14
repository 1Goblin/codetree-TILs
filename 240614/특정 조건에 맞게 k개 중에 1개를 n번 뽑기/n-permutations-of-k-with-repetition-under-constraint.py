# k, n = tuple(map(int, input().split()))

# ans = []

# def choose(num):

#     if num > n:
#         print(*ans, sep=" ")
#         return
    

#     for i in range(1,k+1):
#         if num > 2 and ans[-1] == i and ans[-2] == i :
#             continue
#         ans.append(i)
#         choose(num+1)
#         ans.pop()

# choose(1)

k, n = tuple(map(int, input().split()))

ans = []

def fun(num):

    if num==n:
        print(*ans, sep=" ")
        return
    

    for i in range(1, k+1):
        if num>=2 and i == ans[-1] and i == ans[-2]:
            continue   
        ans.append(i)
        fun(num+1)
        ans.pop()
    

fun(0)