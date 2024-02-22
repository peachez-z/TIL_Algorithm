def solution(x):
    answer = True
    x = str(x)
    xtotal = []
    for i in range(len(x)):
        xtotal.append(int(x[i]))
    print(sum(xtotal))
    s = sum(xtotal)
    if int(x) % s == 0 :
        answer = True
    else: 
        answer = False
    return answer