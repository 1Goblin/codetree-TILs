k, n = tuple(map(int, input().split()))

ans = []

def fun(num):

    if num==n:
        print(*ans, sep=" ")
        return

    
    for i in range(1, k+1):
        ans.append(i)
        fun(num+1)
        ans.pop()
    
fun(0)