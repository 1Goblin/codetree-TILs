a = input()
b = input()

c = ""
d = ""

for i in a:
    if ord(i)>=ord('0') and ord(i)<=ord('9'):
        c+=i

for i in b:
    if ord(i)>=ord('0') and ord(i)<=ord('9'):
        d+=i

print(int(c)+int(d))