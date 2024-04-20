n = int(input())


def a(n):
    if n==0:
        return
    print(n,end=" ")
    a(n-1)

def b(n):
    if n==0:
        return
    b(n-1)
    print(n,end=" ")

b(n)
print()
a(n)