def solution(lottos, win_nums):


    answer = []
    unknownCnt = 0
    matchCnt = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            unknownCnt += 1
        for j in range(len(win_nums)):
            if win_nums[j] == lottos[i]:
                matchCnt += 1

    best = int(min(7 - (unknownCnt + matchCnt), 6))
    worst = int(min(7 - matchCnt, 6))

    answer.append(best)
    answer.append(worst)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))