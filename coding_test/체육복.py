n=10
lost=[8, 10]
reserve=[6, 7, 9]
n2=4
lost2=[3, 1]
reserve2=[2, 4]

def solution(n,lost,reserve):
    real_lost=set(lost)-set(reserve) #잃어버린 사람들
    real_reserve=set(reserve)-set(lost) #여분있는 사람들

    for i in real_reserve:
        if i-1 in real_lost:
            real_lost.remove(i-1)
        elif i+1 in real_lost:
            real_lost.remove(i+1)
    return n-len(real_lost)
    solution(n,lost,reserve)
print("----------------------")
solution(n2,lost2,reserve2)