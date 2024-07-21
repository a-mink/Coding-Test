def solution(n, words):
    answer = []
    # 마지막 단어(끝말잇기 이어지지 않는 단어) 제외.
    for i, j in enumerate(words[:-1]):
        # i + 1 인덱스 값의 정답여부 판별
        if j in words[:i]:
            answer.append(i%n + 1)
            answer.append(i//n + 1)
            break
        elif j[-1] != words[i+1][0]:
            answer.append((i + 1)%n + 1)
            answer.append((i + 1)//n + 1)
            break
    
    # 마지막 단어 점검 및 모두 정답일 케이스
    if answer != []:
        return answer
    elif words[-1] in words[:-1]:
        answer.append((len(words) - 1)%n + 1)
        answer.append((len(words) - 1)//n + 1)
        return answer
    else:
        return [0, 0]