class employee:
    def __init__(self, e_id="", score=0):
        self.e_id = e_id
        self.score = int(score)

def min_score(employees, n):
    p = 0
    for i in range(n):
        if employees[p].score>employees[i].score:
            p = i
    return employees[p].e_id, employees[p].score

employees = []

for i in range(5):
    e_id, score = input().split()
    employees.append(employee(e_id, score))

loweremployee = min_score(employees, 5)
print(loweremployee[0], loweremployee[1])