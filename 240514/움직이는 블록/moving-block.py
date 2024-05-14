n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
cnt = 0
s = 0
for i in arr:
    s+=i
avg = s//len(arr)

arr.sort(reverse=True)

for i in range(len(arr)):
    if arr[i]>avg:
        for j in range(i,len(arr)):
            while(1):
                if arr[j]>=avg or arr[i]<=avg:
                    break
                arr[j]+=1
                arr[i]-=1
                cnt+=1
print(cnt)