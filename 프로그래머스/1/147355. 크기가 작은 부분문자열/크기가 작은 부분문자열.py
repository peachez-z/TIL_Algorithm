def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t)):
        if i+length <= len(t):
            x = t[i:i+length]
            if x <= p:
                answer += 1
    return answer