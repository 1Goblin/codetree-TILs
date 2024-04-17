y = int(input())

def checkyear(year):
    if year%4==0 or (year%100!=0 and year%400==0):
        return True
    else:
        return False
        


if checkyear(y):
    print("true")
else:
    print("false")