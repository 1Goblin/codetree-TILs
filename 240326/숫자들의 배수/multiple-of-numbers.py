n = int(input())
arr = [n]

cnt = 0
for i in range(100):
    arr.append(arr[0]*(i+2))
    if arr[i+1]%5==0:
        cnt+=1
    if cnt==2:
        break
for k in arr:
    print(k,end=" ")