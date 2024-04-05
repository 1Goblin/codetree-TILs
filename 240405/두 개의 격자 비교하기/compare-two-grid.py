n, m = tuple(map(int, input().split()))

arr1 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr2 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr3 =[
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            arr3[i][j]=0
            print(0,end=" ")
        else:
            arr3[i][j]=1
            print(1,end=" ")
    print()