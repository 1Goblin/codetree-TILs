a, b = map(int, input().split())
n = list(map(int, list(input())))

num = 0

for i in range(len(n)):

    num = num*a + n[i]

ans = []

while(1):

    if num<b:
        ans.append(num)
        break
    

    ans.append(num%b)
    num = num//b


for k in ans[::-1]:
    print(k,end="")