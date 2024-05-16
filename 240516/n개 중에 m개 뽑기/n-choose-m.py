n, m = tuple(map(int, input().split()))


ans = []

def comb(num,ch):

    if num > m:
        print(*ans, sep=" ")
        return
    

    for i in range(ch,n+1):
        ans.append(i)
        comb(num+1,i+1)
        ans.pop()


comb(1,1)