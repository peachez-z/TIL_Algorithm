import math

def solution(n):
    answer = 0
    x = int((n+1)**0.5)
    for i in range(1,x+1):
        if i*i == n:
            answer = (i+1)*(i+1)
    if answer == 0 :
        answer = -1
    return answer