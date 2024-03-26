arr = list(map(int, input().split()))


for i in range(2,10):
    arr.append((arr[i-2] + arr[i-1])%10)

for k in arr:
    print(k,end=" ")