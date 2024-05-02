n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

a1, a2 = tuple(map(int, input().split()))
b1, b2 = tuple(map(int, input().split()))

a1 = a1-1
a2 = a2-1
b1 = b1-1
b2 = b2-1 

temp = []

for i in range(n):
    if i>=a1 and i<=a2:
        continue
    temp.append(arr[i])


temp2 = []

for j in range(len(temp)):
    if j>=b1 and j<=b2:
        continue
    temp2.append(temp[j])

print(len(temp2))
for k in temp2:
    print(k)