def solution(sizes):
    answer = 0
    max_w , max_h = 0 , 0
    for i in sizes:
        a, b = i
        max_w = max(max_w, max(a,b))
        max_h = max(max_h, min(a,b))
    answer  = max_w * max_h
    return answer