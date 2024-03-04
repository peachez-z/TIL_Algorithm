def solution(n, m):
    answer = []
    # 최대공약수 계산
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # 최소공배수 계산
    gcd_result = find_gcd(n, m)
    lcm_result = (n * m) // gcd_result

    answer.append(gcd_result)
    answer.append(lcm_result)

    return answer