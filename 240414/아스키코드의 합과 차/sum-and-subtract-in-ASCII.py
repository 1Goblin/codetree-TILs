a, b = tuple(map(str, input().split()))



if a>b:
    m = ord(a)-ord(b)
else:
    m = ord(b) - ord(a)

p = ord(a) + ord(b)
print(p, m)