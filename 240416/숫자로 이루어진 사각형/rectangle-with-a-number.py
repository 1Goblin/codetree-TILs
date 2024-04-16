n = int(input())

def pr (n):
    j = 1
    for i in range(n):
        for i in range(n):
            print(j,end=" ")
            j+=1
            if j==10:
                j=1
        print()


pr(n)