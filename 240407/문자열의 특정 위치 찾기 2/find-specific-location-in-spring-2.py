arr2 = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()
cnt = 0

for i in range(5):
    c = False
    for j in range(2,4):
        if n==arr2[i][j]:
            c = True
    if c==True:
        print(arr2[i])
        cnt+=1
print(cnt)