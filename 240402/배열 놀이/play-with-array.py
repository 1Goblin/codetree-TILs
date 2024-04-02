n, q = tuple(map(int, input().split()))
values = list(map(int, input().split()))

for i in range(1,n+1):
    arr = []
    arr = list(map(int, input().split()))
    a = int(arr[0])
    b = int(arr[1])

    if a==1:
        print(values[b-1])
    elif a==2:
        if b in values:
            print((values.index(b)+1))
        else:
            print(0)
    elif a==3:
        c = int(arr[2])
        for i in range(b, c+1):
            print(values[i-1],end=" ")
        print()