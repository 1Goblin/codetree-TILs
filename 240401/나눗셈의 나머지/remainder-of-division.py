arr = input().split()
a = int(arr[0])
b = int(arr[1])

count = [0] * b
s = 0
while a > 1:
    count[a % b] += 1
    a = a // b

for k in range(b):
    s += count[k] * count[k]

print(s)