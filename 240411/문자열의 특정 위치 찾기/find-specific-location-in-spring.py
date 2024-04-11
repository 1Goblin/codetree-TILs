a = input().split()

if a[1] in a[0]:
    print(a[0].index(a[1]))
else:
    print("No")