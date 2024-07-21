
def solution(n, words):
    for i in range(1, len(words)):
        # 현재 단어의 첫 글자가 이전 단어의 마지막 글자와 다르거나, 현재 단어가 이전에 이미 나온 경우
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]
