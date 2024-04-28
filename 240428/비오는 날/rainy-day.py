n = int(input())

class weather:
    def __init__(self, date, dw, wt):
        self.date = date
        self.dw = dw
        self.wt = wt


arr = []
rain_day = 0
for i in range(n):
    date, dw, wt = input().split()
    arr.append(weather(date, dw, wt))
    if wt == "Rain":
        rain_day = i
        break
    

print(f"{arr[rain_day].date} {arr[rain_day].dw} {arr[rain_day].wt}")