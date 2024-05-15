a1, b1, a2, b2 = tuple(map(int, input().split()))
x1, y1, x2, y2 = tuple(map(int, input().split()))


width = max(x2,a2) - min(a1,x1)
height = max(b2,y2) - min(b1,y1)

print(width*height)