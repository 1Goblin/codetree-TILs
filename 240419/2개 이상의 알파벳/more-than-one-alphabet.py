a = input()


def stcheck(st):
    cnt = 0
    for i in range(len(st)-1):
        for j in range(i+1,len(st)):
            if st[i]==st[j]:
                cnt+=1
        if cnt>=2:
            return True
        cnt = 0
    return False

if stcheck(a):
    print("Yes")
else:
    print("No")