n, k = map(int, input().split())  # n번 반복, 1부터 k까지의 숫자를 사용
answer = []

def choose(curr_num):
    if curr_num == n + 1:  # n번 숫자를 선택했으면 출력
        print(*answer)
        return

    for i in range(1, k + 1):  # 1부터 k까지의 숫자를 선택
        answer.append(i)
        choose(curr_num + 1)  # 다음 숫자 선택
        answer.pop()  # 선택을 취소하고 다른 숫자 선택

choose(1)  # 재귀 함수 시작