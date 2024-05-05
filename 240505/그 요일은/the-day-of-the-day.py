m1, d1, m2, d2 = map(int, input().split())
i_week = input()

d = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if m1==m2:
    day = d2 - d1
else:
    day = num_of_days[m1]-d1 + d2
    for i in range(m1+1,m2):
        day+=num_of_days[i]



ans = day//7
for i,w in enumerate(d):
    if i_week == w and i>=day%7:
        ans+=1

print(ans)