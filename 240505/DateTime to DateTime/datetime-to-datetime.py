a, b, c = map(int, input().split())

fu_m = (a*24*60) + (b*60) + c
cu_m = (11*24*60) + (11*60) + 11

an_m = fu_m - cu_m

if an_m < 0:
    print(-1)
else:
    print(an_m)