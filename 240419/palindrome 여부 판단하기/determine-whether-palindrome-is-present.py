st = input()

def palin(st):
    string = ""
    for i in st[::-1]:
        string+=i
    return string

if st==palin(st):
    print("Yes")
else:
    print("No")