n = int(input())
arr = list(map(int, input().split()))

new_arr=[i*i for i in arr]
for i in range(n):
    print(new_arr[i],end=" ")