def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False
    for i in range(len(s)):
        if not s[i].isdigit() :
            return False
    return answer