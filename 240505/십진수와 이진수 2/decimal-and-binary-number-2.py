n = list(map(int, list(input())))

num = 0

for i in range(len(n)):

    num = num * 2 + n[i]

num = num* 17
ans = []

while(1):

    if num<2:
        ans.append(num)
        break

    ans.append(num%2)
    num = num//2

for k in ans[::-1]:
    print(k,end="")