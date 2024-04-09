n = int(input())

arr = [
    input()
    for _ in range(n)
]

c = input()
a = 0
b = 0

for i in arr:
    if i[0]==c:
        a+=1
        b+=len(i)

print(f"{a} {b/a:.2f}")