a,b,x,y = tuple(map(int, input().split()))

move = b-a

move = min(move, abs(a-x)+abs(y-b))
move = min(move, abs(a-y)+abs(x-b))


print(move)