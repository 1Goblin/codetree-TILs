string = input()

cnt = 0
st = ""

for i in range(0,len(string)-1):
    if string[i]==string[i+1]:
        cnt+=1
    else:
        st+=string[i]+str(cnt+1)
        cnt=0
    if i==len(string)-2:
        st+=string[i]+str(cnt+1)

print(len(st))
print(st)