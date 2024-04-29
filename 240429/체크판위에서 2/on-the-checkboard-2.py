r, c = map(int, input().split())
arr = [
    list(map(str, input().split()))
    for _ in range(r)
]

cnt = 0
p_word = arr[0][0]


for i in range(1, r-2):
    for j in range(1, c-2):
        p_word = arr[0][0]
        if p_word != arr[i][j]:
            p_word = arr[i][j]
            for m in range(i+1, r-1):
                for n in range(j+1, c-1):
                    p_word = arr[i][j]
                    if p_word != arr[m][n] and p_word == arr[r-1][c-1]:
                        p_word = arr[m][n]
                        cnt+=1

print(cnt)