arr = input().split()
a = int(arr[0])
b = int(arr[1])

for i in range(1,10,1):
    if b%2==0:
        for j in range(b,a-1,-2):
            print(f"{j} * {i} = {j*i}",end="")
            if j>a:
                print(" / ",end="")
    else:
        for k in range(b-1,a-1,-2):
            print(f"{j} * {i} = {j*i}",end="")
            if j>a:
                print(" / ",end="")
    print()