n1 = input()
n2 = input()
n3 = input()

if len(n1)>len(n2):
    if len(n2)>len(n3):
        print(len(n1)-len(n3))
    elif len(n1)>len(n3):
        print(len(n1)-len(n2))
    else:
        print(len(n3)-len(n2))
elif len(n2)>len(n3):
    if len(n3)>len(n1):
        print(len(n2)-len(n1))
    else:
        print(len(n2)-len(n3))
elif len(n3)>len(n2):
    if len(n1)>len(n2):
        print(len(n3)-len(n2))
    else:
        print(len(n3) - len(n1))