n = int(input())
arr = list(map(float, input().split()))

s = 0
for i in range(n):
    s +=arr[i]
g = s/n
print(f"{g:.1f}")
if g>=4.0:
    print("Perfect")
elif g>=3.0:
    print("Good")
else:
    print("Poor")