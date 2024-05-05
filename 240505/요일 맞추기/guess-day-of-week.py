m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = {
    0 : "Mon",
    1 : "Tue",
    2 : "Wed",
    3 : "Thu",
    4 : "Fri",
    5 : "Sat",
    6 : "Sun"
}

if m1==m2:
    day = d2-d1
elif m1<m2:
    day = num_of_days[m1]-d1 + d2
    for i in range(m1+1,m2):
        day+=num_of_days[i]
else:
    day = num_of_days[m2]-d2 + d1
    for i in range(m2+1,m1):
        day+=num_of_days[i]

print(d[day%7])