def solution(d, budget):
    answer = 0
    while (True):
        if len(d) == 0:
            break
        if budget < min(d):
            break
        else:
            budget -= min(d)
            d.remove(min(d))
            answer += 1
    return answer
d = [2,2,3,3]
budget = 10
print(solution(d,budget))