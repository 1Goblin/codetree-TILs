n = input()

f = ord("A")
m = ord("a")
e = ord("z")

for i in n:
    if ord(i)>=f and ord(i)<m:
        print(i,end="")
    elif ord(i)>=m and ord(i)<=e:
        print(chr(ord(i)-m+f),end="")
    else:
        continue