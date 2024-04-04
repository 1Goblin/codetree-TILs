arr2 = [
    list(map(str,input().split()))
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        arr2[i][j] = chr(ord(arr2[i][j])-32)
        print(arr2[i][j],end=" ")
    print()