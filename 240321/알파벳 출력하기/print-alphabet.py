n = int(input())
x = 'A'

for i in range(n):
    for j in range(i+1):
        print(x,end="")
        x = chr(ord(x)+1)
        if x=='Z':
            x='A'
    print()