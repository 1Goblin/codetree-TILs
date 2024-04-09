string = input()

cnt = 0

st = ""

ca = string[0]

for i in range(1, len(string)):
    if ca==string[i]:
        cnt+=1
        
    else:
        st+=ca+str(cnt+1)
        ca=string[i]
        cnt=0
    
st+=ca+str(cnt+1)



print(len(st))
print(st)