a = input()


def stcheck(st):
    arr = []
    for i in st:
        if i not in arr:
            arr.append(i)
    if len(arr)>=2:
        return True
    else:
        return False

if stcheck(a):
    print("Yes")
else:
    print("No")