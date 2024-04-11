a = input()
b = input()

c = 0

for i in range(len(a)-1):
    for j in range(len(b)):
        if a[i+j]!=b[j]:
            break
        if j==len(b)-1:
            c+=1
print(c)