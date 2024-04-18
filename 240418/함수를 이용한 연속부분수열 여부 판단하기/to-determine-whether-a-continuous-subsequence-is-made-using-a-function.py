a, b = map(int, input().split())

n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

def snum(n1, n2, a, b):
    for i in range((a-b)):
        for j in range(b):
            if n1[i+j]!=n2[j]:
                break
            if j==(len(n2)-1):
                return True
    
    return False


if snum(n1, n2, a, b):
    print("Yes")
else:
    print("No")