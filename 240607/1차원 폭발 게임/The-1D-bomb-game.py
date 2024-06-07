n, m = tuple(map(int, input().split()))

arr = [
    int(input())
    for _ in range(n)
]

sameN = []

def pboom(i):
    global end
    for k in range(i-1,i-1-len(sameN),-1):
        arr[k] = 0
        end = False

def boom():
    global sameN
    sameN = []
    sameN.append(arr[0])
    for i in range(1, len(arr)):
        if sameN[-1] == arr[i]:
            sameN.append(arr[i])
        else:
            if len(sameN) >= m:
                pboom(i)
            sameN = []
            sameN.append(arr[i])

        if len(arr)-1==i:
            if len(sameN) >= m:
                pboom(i+1)
            sameN = []
            sameN.append(arr[i])
    if len(arr) == 1 and m==1:
        arr.pop()


def init():
    temp = []
    global arr
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        temp.append(arr[i])
    arr = temp


while(1):
    end = True
    if len(arr) != 0:
        boom()
        init()

    if end:
        break


if len(arr) == 0:
    print(0)
else:
    print(len(arr))
    for i in arr:
        print(i)