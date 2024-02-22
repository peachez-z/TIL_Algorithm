def solution(x, n):
    answer = [x]
    a = x
    for i in range(n-1):

        a += x
        answer.append(a)
    return answer