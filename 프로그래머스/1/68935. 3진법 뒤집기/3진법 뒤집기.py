def thr(n):
    if n == 0 :
        return '0'
    result=''
    while n > 0 :
        n, x = n//3, n%3
        result = str(x) + result
    return result
    
def solution(n):
    answer = int(thr(n)[::-1],3)
    return answer