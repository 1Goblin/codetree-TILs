k, n = tuple(map(int, input().split()))

ans = []

def choose(num):

    if num > n:
        print(*ans, sep=" ")
        return
    

    for i in range(1,k+1):
        if num-2 > 0 and ans[-1] == i and ans[-2] == i :
            continue
        ans.append(i)
        choose(num+1)
        ans.pop()

choose(1)