def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_rest = find_max(arr, n - 1)
        return max(arr[n - 1], max_rest)

n = int(input())
arr = list(map(int, input().split()))

result = find_max(arr, n)
print(result)