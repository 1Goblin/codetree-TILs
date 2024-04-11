n = int(input())

arr = list(map(str, input().split()))

st=""

c=0

for i in arr:
    for j in range(len(i)):
        st+=i[j]
        if len(st)==5:
            print(st)
            st=""

print(st)