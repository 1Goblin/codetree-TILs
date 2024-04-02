a, b = tuple(map(int, input().split()))
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
an = "No"

for i in range(a):
    if n1[i]==n2[0]:
        for j in range(b):
            if (a-i)>b:
                if n1[i+j]==n2[j]:
                    an ="Yes"
                else:
                    an= "No"

print(an)