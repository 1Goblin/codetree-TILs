n, m , k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

m = m-1
ans = []
answer = 0


def fun(num):
    global answer
    if num==n:
        an = 0
        for i in range(k):
            s = 0
            for j in range(n):
                if ans[j] == i:
                    s+=arr[j]
            if s>=m:
                an+=1
        answer = max(answer, an)
        return

    
    for i in range(k):
        # s = 0
        # for j in range(num):
        #     if ans[j] == i:
        #         s+=arr[j]
        # if s>=k:
        #     continue
        ans.append(i)
        fun(num+1)
        ans.pop()

fun(0)

print(answer)