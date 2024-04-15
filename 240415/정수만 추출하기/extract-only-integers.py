a, b = input().split()

c=""
d=""

for i in a:
    if ord(i)>=ord("0") and ord(i)<=ord("9"):
        c+=i
    else:
        break

for i in b:
    if ord(i)>=ord("0") and ord(i)<=ord("9"):
        d+=i
    else:
        break
print(int(c)+int(d))