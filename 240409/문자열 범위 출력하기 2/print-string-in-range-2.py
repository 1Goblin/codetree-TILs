string = input()
n = int(input())

for i in string[len(string):len(string)-n-1:-1]:
    print(i,end="")