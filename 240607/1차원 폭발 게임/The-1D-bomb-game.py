n, m = tuple(map(int, input().split()))

arr = [
    int(input())
    for _ in range(n)
]

sameN = []
ans = []
end =0

def init():
    for i in range(len(arr)):
        if arr[i]==0:
            continue
        temp.append(arr[i])


def boom(i):
    for j in range(i-1,i-1-len(sameN), -1):
        arr[j] = 0

while(1):
    for i in range(len(arr)):
        if len(sameN)==0 or sameN[-1] == arr[i]:
            sameN.append(arr[i])
        else:
            if len(sameN) >= m:
                temp = []
                boom(i)
                init()
                arr = temp
                break
            else:
                sameN = []
                sameN.append(arr[i])
        if i==len(arr)-1:
            end = 1
    if end==1 or len(arr)==0:
        break


if len(arr) == 0:
    print(0)
else:
    for i in arr:
        print(i)