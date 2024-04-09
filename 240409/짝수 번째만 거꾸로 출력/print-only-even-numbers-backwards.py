string = input()

arr = ""

for i in range(len(string)):
    if i%2==1:
        arr+=string[i]
print(arr[::-1])