x1, x2, x3, x4 = tuple(map(int, input().split()))

ans = 0

def check(x1,x2, k):
    return x1 <= k and x2 >= k


if check(x1,x2,x3):
    ans = 1

if check(x1,x2,x4):
    ans = 1

if check(x3,x4,x1):
    ans = 1

if check(x3,x4,x2):
    ans = 1

if ans==1:
    print("intersecting")
else:
    print("nonintersecting")