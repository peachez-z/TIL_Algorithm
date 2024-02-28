def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    total = sum(num)
    answer = -1
    for i in range(len(numbers)):
        if numbers[i] in num : 
            total -= numbers[i]
    return total