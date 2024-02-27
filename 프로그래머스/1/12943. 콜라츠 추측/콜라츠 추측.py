def solution(num):
    answer = 0
    if num == 1 :
        return answer
    else:
        while num > 1 and answer < 500:
            if num == 0:
                break
            if num % 2 == 0 :
                num = num//2
                answer += 1
            elif num % 2 == 1 :
                num = (num*3) + 1
                answer += 1
        if answer >= 500: 
            return -1
        else:
            return answer
    
   