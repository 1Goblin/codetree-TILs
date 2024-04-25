n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    max_num = 0
    if max_num<arr[i]+arr[(2*n-1)-i]:
        max_num = arr[i]+arr[(2*n-1)-i]

print(max_num)