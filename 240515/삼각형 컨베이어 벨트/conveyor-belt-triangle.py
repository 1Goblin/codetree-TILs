n, t = tuple(map(int, input().split()))

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

def push():
    temp = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0]=temp


arr = l+r+d

for _ in range(t):
    push()

for i,value in enumerate(arr):
    print(value,end=" ")
    if i%n==(n-1):
        print()