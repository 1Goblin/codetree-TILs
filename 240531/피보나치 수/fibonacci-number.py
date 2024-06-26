# n = int(input())

# dp = [1] * (n+1)


# for i in range(3,n+1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])

n = int(input())

mem = [-1] * (n+1)

def f(num):
    if mem[num] != -1:
        return mem[num]

    if num<=2:
        return 1
    
    mem[num] = f(num-1) + f(num-2)

    return mem[num]

print(f(n))