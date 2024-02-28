def solution(arr):
    if len(arr) == 1:
        return [-1]
    answer = []
    num = min(arr)
    arr.remove(num)
    return arr