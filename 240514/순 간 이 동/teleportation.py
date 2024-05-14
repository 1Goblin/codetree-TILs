a,b,x,y = tuple(map(int, input().split()))

move = abs(b-a)

move = min(move, abs(a-x)+abs(y-b))
move = min(move, abs(a-y)+abs(x-b))

86 84 15 78

print(move)