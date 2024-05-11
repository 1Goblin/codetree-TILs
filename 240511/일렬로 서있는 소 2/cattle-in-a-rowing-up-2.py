n = int(input())
arr = list(map(int, input().split()))

def aaa(a,b,c):
    return a<=b and b<=c


cnt = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if aaa(arr[i],arr[j],arr[k]):
                cnt+=1
            

print(cnt)