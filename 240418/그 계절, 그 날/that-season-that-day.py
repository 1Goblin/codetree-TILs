y, m, d = map(int, input().split())

def ckSeason(m):
    if m>=3 and m<=5:
        return "Spring"
    elif m>=6 and m<=8:
        return "Summer"
    elif m>=9 and m<=11:
        return "Fall"
    else:
        return "Winter"

def ckyoon(y):
    if y%4!=0 or (y%4==0 and y%100==0 and y%400!=0):
        return False
    else:
        return True

def ckmonth(y,m, d):
    if m==2:
        if ckyoon(y) and d<30:
            return True
        elif d<29:
            return True
    elif (m==4 or m==6 or m==9 or m==11) and d<31:
        return True
    elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d<32:
        return True
    else:
        return False

if ckmonth(y,m,d):
    print(ckSeason(m))
else:
    print(-1)