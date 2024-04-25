n = int(input())
arr = list(map(int, input().split()))
max_num = 0
arr.sort()

for i in range(n):
    if max_num<arr[i]+arr[(2*n-1)-i]:
        max_num = arr[i]+arr[(2*n-1)-i]

print(max_num)