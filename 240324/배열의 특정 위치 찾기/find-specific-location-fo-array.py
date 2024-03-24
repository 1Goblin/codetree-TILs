arr = list(map(int, input().split()))

a = arr[1::2]
b = arr[2::3]
c = sum(a)
d = sum(b)
e = d/3

print(f"{c} {e:.1f}")