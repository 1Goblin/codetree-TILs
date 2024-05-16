n = int(input())

ans = []
visited = [False] * (n+1)


def p(num):

    if num > n:
        print(*ans, sep=" ")
        return
    
    for i in range(1,n+1):

        if visited[i] == True:
            continue
        ans.append(i)
        visited[i] = True

        p(num+1)

        ans.pop()
        visited[i] = False



p(1)