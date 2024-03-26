n = int(input())
arr = list(map(int,input().split()))
count = [0]*10

for i in range(n):
    count[arr[i]]+=1

for k in range(1,10):
    print(count[k])