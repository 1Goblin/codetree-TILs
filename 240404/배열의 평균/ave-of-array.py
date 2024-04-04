s = 0
m = 0
arr2 = []
for i in range(2):
    arr = list(map(int, input().split()))
    print(f"{sum(arr)/len(arr):.1f}", end=" ")

    arr2.append(arr)
    s+=sum(arr)
print()

for i in range(4):
    m = 0
    for j in range(2):
        m += arr2[j][i]
    print(f"{m/2:.1f}",end=" ")
print()

print(f"{s/8:.1f}")