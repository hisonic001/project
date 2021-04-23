participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    answer = ""
    ran = range(len(c))
    if p[-1] != c[-1]:
        answer = p[-1]
        return answer
    else:
        for num in ran:
            if p[num] != c[num]:
                answer = p[num]
                return answer

    
solution(participant,completion)