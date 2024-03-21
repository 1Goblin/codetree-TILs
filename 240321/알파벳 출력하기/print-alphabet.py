n = int(input())
x = 'A'

for i in range(n):
    for j in range(i+1):
        print(x,end="")
        if x=='Z':
            x='@'
        x = chr(ord(x)+1)
    print()