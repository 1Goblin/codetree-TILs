n, t = tuple(map(int, input().split()))

arr = []

for i in range(2):
    ar = list(map(int, input().split()))
    arr+=ar


def push():
    temp = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp


for i in range(t):
    push()

for i,j in enumerate(arr):
    print(j,end=" ")
    if i==n-1:
        print()