arr = input().split()
a = int(arr[0])
b = int(arr[1])

count =[0]*10
s = 0
for i in range(100):

    count[a%b]+=1
    a=a//b
    if a==0:
        break

for k in range(0,10):
    s+=count[k]*count[k]

print(s)