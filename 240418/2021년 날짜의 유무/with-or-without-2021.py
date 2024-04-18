m, d = map(int, input().split())

def cm(m):
    if m>0 and m<13:
        return True
    else:
        False

def cd(m,d):
    if m==2 and d<29:
        return True
    elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d<32:
        return True
    elif (m==4 or m==6 or m==9 or m==11) and d<31:
        return True

    return False




if cm(m) and cd(m,d):
    print("Yes")
else:
    print("No")