a = input()
b = input()

while a.find(b) != -1:
    start_pos = a.find(b)
    a = a[:start_pos] + a[start_pos + len(b):]
print(a)