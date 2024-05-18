from collections import deque

n, m, q = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def can_go(r):
    return r>=0 and r<n and visited[r] == 0

dq = deque()

move = []

def check(br,cr):
    for i in range(m):
        if arr[br][i] == arr[cr][i]:
            return True
    return False


def push_l(r):
    temp = arr[r][-1]
    for i in range(m-1,-1,-1):
        arr[r][i] = arr[r][i-1]
    arr[r][0] = temp

def push_r(r):
    temp = arr[r][0]
    for i in range(0,m-1):
        arr[r][i] = arr[r][i+1]
    arr[r][-1] = temp


for i in range(q):
    r, d = input().split()
    move.append((int(r)-1,d))

dxs = [1,-1]

def bfs():
    global p
    global k 
    while dq:
        r = dq.popleft()
        for dx in dxs:
            ndx = r+dx
            if can_go(ndx):
                visited[ndx] = 1
                dq.append(ndx)
                if check(r,ndx) and p==(ndx%2):
                    if k==1:
                        push_r(ndx)
                    else:
                        push_l(ndx)
                elif check(r,ndx) and p!=(ndx%2):
                    if k==1:
                        push_l(ndx)
                    else:
                        push_r(ndx)
                
for i in move:
    visited =[0] * n

    if i[1] == 'R':
        p = i[0]%2
        k = 1
        push_r(i[0])
        visited[i[0]] = 1
        dq.append(i[0])
        bfs()
    else:
        p = i[0]%2
        k = 0
        push_l(i[0])
        visited[i[0]] = 1
        dq.append(i[0])
        bfs()


for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()