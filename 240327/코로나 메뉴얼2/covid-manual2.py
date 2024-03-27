count = [0]*4
a = 0

for i in range(3):
    arr = input().split()
    a = arr[0]
    b = int(arr[1])

    if a=="Y" and b>=37:
        count[0]+=1
    elif a=="N" and b>=37:
        count[1]+=1
    elif a=="Y" and b<37:
        count[2]+=1
    else:
        count[3]+=1
    
for k in range(4):
    print(count[k],end=" ")
if count[0]>=2:
    print("E")