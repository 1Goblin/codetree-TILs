n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def a1(r,c):
    return r+1<n and c+1<m

def a2(r,c):
    return r+1<n and c-1>=0

def a3(r,c):
    return (r+2)<n

def a4(r,c):
    return (c+2)<m



max_sum = 0


for i in range(n):
    for j in range(m):
        if a1(i,j):
            s1 = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
            max_sum = max(s1,max_sum)

for i in range(n):
    for j in range(m):
        if a1(i,j):
            s2 = arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
            max_sum = max(s2,max_sum)

for i in range(n):
    for j in range(m):
        if a2(i,j):
            s3 = arr[i][j] + arr[i+1][j] + arr[i+1][j-1]
            max_sum = max(s3,max_sum)


for i in range(n):
    for j in range(m):
        if a2(i,j):
            s4 = arr[i][j] + arr[i][j-1] + arr[i+1][j-1]
            max_sum = max(s4,max_sum)

for i in range(n):
    for j in range(m):
        if a3(i,j):
            s5 = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            max_sum = max(s5,max_sum)

for i in range(n):
    for j in range(m):
        if a4(i,j):
            s6 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            max_sum = max(s6,max_sum)

print(max_sum)