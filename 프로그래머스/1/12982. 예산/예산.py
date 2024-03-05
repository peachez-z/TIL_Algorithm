def solution(d, budget):
    # 부분합이 budget 이하인 가장 많은 부분은 몇 개?
    d.sort()
    start = 0
    end = 1
    pre_sum = [0]*(len(d)+1)
    for i in range(1,len(pre_sum)):
        pre_sum[i] = pre_sum[i-1] + d[i-1]

    answer = 0
    # 시작지점이 끝 지점이 아닐 때    
    while start < len(d):
        # 특정 구간합이 budget 이하일 때
        if end <= len(d) and pre_sum[end] - pre_sum[start] <= budget:
            if end-start > answer:
                answer = end-start
            # 구간 늘리기
            end += 1
        # 특정 구간 합이 budget 이상일 때 / end가 끝까지 갔을 때
        else:
            # 끝까지 갔다면 start를 뒤로 밀기
            start += 1
    return answer