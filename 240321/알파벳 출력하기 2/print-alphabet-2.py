n = int(input())
x = 'A'

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print(x,end=" ")
        x = chr(ord(x)+1)
        if ord(x) > ord('Z'):
            x = 'A'
    
    print()