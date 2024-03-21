n = int(input())
x = 'A'

for i in range(n):
    for j in range(n):
        print(x,end="")
        x=chr(ord(x)+1)
    print()