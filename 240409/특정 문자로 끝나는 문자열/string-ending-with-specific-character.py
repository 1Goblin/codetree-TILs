string = [
    input()
    for _ in range(11)
]
c = 0

for i in string[0:10:1]:
    if i[-1]==string[-1]:
        print(i)
        c+=1
if c==0:
    print("None")