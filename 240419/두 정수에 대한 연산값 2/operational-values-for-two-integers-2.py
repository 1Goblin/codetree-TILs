a, b =tuple(map(int,input().split()))

def change(a, b):
    if a<b:
        a+=10
        b*=2
    else:
        a*=2
        b+=10

    return a,b

a, b = change(a,b)

print(a, b)