n, m = tuple(map(int, input().split()))

arr =[ [] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]

cnt = 0

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    arr[x].append(y)
    arr[y].append(x)

def dfs(vertex):
    global cnt
    for curr_v in arr[vertex]:
        if not visited[curr_v]:
            cnt+=1
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)

print(cnt-1)