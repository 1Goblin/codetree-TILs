string = input()

st = ""
cnt = 0
for i in range(len(string)-1):

    if string[i]==string[i+1]:
        cnt+=1
        if i==len(string)-2:
            st+=string[i]+str(cnt+1)
    else:
        st+=string[i]+str(cnt+1)
        cnt=0
        if i==len(string)-2:
            st+=string[i+1]+"1"


if len(string)==1:
    st=string+"1"

print(len(st))
print(st)