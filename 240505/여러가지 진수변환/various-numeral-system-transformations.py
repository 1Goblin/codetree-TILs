def convert_base(N, B):
    if B == 8:
        return oct(N)[2:]  # oct() 함수 사용, 앞의 '0o' 제거
    elif B == 4:
        return decimal_to_base_4(N)  # 4진수 변환 함수 호출
    else:
        return "Unsupported Base"

def decimal_to_base_4(N):
    if N == 0:
        return "0"
    digits = []
    while N:
        digits.append(int(N % 4))
        N //= 4
    digits.reverse()
    return ''.join(map(str, digits))  # 리스트를 문자열로 변환

# 사용자 입력
N, B = tuple(map(int, input().split()))

# 결과 출력
result = convert_base(N, B)
print(f"{result}")