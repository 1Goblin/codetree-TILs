class meet:
    def __init__(a, code, av, time):
        a.c = code
        a.a = av
        a.t = time




c, a, t = input().split()

abc = meet(c,a,t)

print(f"secret code : {abc.c}")
print(f"meeting point : {abc.a}")
print(f"time : {abc.t}")