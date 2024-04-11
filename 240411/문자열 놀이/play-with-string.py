m, n = input().split()

n = int(n)
m = list(m)
c =""

for i in range(n):
    arr = input().split()

    if arr[0]=="1":
        c= m[int(arr[1])-1]
        m[int(arr[1])-1] = m[int(arr[2])-1]
        m[int(arr[2])-1] = c
        print("".join(m))
    elif arr[0]=="2":
        for i in range(len(m)):
            if m[i]==arr[1]:
                m[i]=arr[2]
        print("".join(m))