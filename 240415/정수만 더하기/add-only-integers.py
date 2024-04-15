n = input()
p = 0

for i in n:
    if ord(i)>ord("0") and ord(i)<ord("9"):
        p+=int(i)

print(p)