n = int(input())

class weather:
    def __init__(self, date, dw, wt):
        self.date = date
        self.dw = dw
        self.wt = wt


arr = []
rain_day = 0
md = ":"
for i in range(n):
    date, dw, wt = input().split()
    arr.append(weather(date, dw, wt))
    if wt == "Rain" and md>date:
        rain_day = i
        md = date
    

print(f"{arr[rain_day].date} {arr[rain_day].dw} {arr[rain_day].wt}")