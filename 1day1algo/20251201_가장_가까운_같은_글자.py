# https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=python3#

def solution(s):
    answer = []
    alpha = [-1 for i in range(ord('z') - ord('a') + 1)]
    for index, i in enumerate(s) : 
        if alpha[ord(i) - ord('a')] == -1 : 
            answer.append(-1)
            alpha[ord(i) - ord('a')] = index
        else : 
            answer.append(index - alpha[ord(i) - ord('a')])
            alpha[ord(i) - ord('a')] = index
    return answer