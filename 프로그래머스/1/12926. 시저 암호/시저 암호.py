def solution(s, n):
    result = ''
    for char in s:
        if char.isalpha():  # 알파벳인 경우에만 처리
            if char.isupper():  # 대문자인 경우
                result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:  # 소문자인 경우
                result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            result += char  # 알파벳이 아닌 경우 그대로 추가
    
    return result