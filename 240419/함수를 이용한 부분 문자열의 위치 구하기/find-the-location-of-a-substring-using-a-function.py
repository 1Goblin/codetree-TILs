a = input()
b = input()

def check():
    for i in range(len(a)-len(b)+1):
        for j in range(len(b)):
            if a[i+j]!=b[j]:
                break
            if j==len(b)-1:
                return i
    return "-1"



print(check())