code, color, second = input().split()

class boom:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    

b1 = boom(code, color, second)

print(f"code : {b1.code}\ncolor : {b1.color}\nsecond : {b1.second}")