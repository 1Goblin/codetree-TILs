n = int(input())
arr = list(map(int, input().split()))

class number:
    def __init__(self, number, pos):
        self.number = number
        self.pos = pos

numbers = []

for i in range(n):

    numbers.append(number(arr[i], i+1))

sort_nums = sorted(numbers, key=lambda x: x.number)


for i in range(n):
    for j in range(n):
        if numbers[i].number==sort_nums[j].number:
            print(j+1,end=" ")
            sort_nums[j].number = 0
            break