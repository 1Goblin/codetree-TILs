n = input()

for i in n:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        print(chr(ord(i)-ord('A')+ord('a')),end="")
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
        print(chr(ord(i)-ord('a')+ord('A')),end="")