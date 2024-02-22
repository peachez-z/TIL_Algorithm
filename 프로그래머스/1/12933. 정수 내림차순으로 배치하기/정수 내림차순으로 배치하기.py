def solution(n):
    answer = 0
    n = str(n)
    total = []
    for i in range(len(n)):
        total.append(int(n[i]))
    total = sorted(total)
    total = total[::-1]
    answer = ''.join(map(str,total))
    return int(answer)