m1, d1, m2, d2 = list(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans = num_of_days[m1] - d1 + d2 +1

for i in range(m1+1,m2):

    ans+= num_of_days[i]


print(ans)