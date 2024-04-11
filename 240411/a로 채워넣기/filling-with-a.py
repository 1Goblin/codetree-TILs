n = input()

st = n[:1] + "a" + n[2:len(n)-2] + "a" + n[len(n)-1:]
print(st)