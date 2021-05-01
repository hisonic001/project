from collections import deque
def solution(prices):
    que = deque(prices)
    answer=[]
    sec =0
    while que:
        num = que.popleft()
        for i in que:
            if num > i :
                sec +=1
                break
            sec+=1
        answer.append(sec)
        sec=0
    return answer
