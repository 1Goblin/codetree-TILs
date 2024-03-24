arr = list(map(int, input().split()))
s1 = 0
s2 = 0
c = 0
for i in arr[0::2]:
    s1+=i
for i in arr[1::2]:
    s2+=i

if s1>=s2:
    c=s1-s2
else:
    c=s2-s1
print(c)