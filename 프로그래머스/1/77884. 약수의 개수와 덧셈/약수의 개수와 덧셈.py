def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        count = 0  # 각 숫자마다 약수의 개수를 새로 초기화
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            ans += i
        else:
            ans -= i
    return ans