n1, n2 = input().split()

if len(n1)>len(n2):
    print(n1, len(n1))
elif len(n1)<len(n2):
    print(n2, len(n2))
else:
    print("same")