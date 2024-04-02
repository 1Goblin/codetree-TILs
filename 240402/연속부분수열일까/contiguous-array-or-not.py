a, b = tuple(map(int, input().split()))
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
c = 0
an = "Yes"
for i in n2:
    if i in n1:
        c = n1.index(i)
        for j in range(c,b+1):
            if n1[j]==n2[j-c]:
                an="Yes"
            else:
                an="No"
    else:
        an="No"
print(an)