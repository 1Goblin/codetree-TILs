n = int(input())
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)

max_n = 0

for i in range(len(arr)):

    if i==0 or arr[i] != arr[i-1]:
        cnt=1
    else:
        cnt+=1

    if max_n < cnt:
            max_n = cnt


print(max_n)