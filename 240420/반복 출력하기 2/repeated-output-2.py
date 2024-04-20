n = int(input())

def prt(n):
    if n==0:
        return
    prt(n-1)
    print("HelloWorld")

prt(n)