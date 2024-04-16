n = input()

def pf(n):
    if int(n)%2==0 and (int(n[0])+int(n[1]))%5==0:
        return "Yes"
    else:
        return "No"


print(pf(n))