s = input()
s = list(s)


for _ in range(len(s)-1):
    n = int(input())
    if n>len(s):
        s.pop(-1)
        s = "".join(s)
        print("".join(s))
        s = list(s)
    else:
        s.pop(n)
        s = "".join(s)
        print("".join(s))
        s = list(s)