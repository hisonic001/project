import collections
from math import prod
num_list=[1,2,3]

def possibilities(num_list):
    times=0
    num_list=[i+1 for i in num_list]
    return prod(num_list)-1

def solution(clothes):
    cloth_list=collections.defaultdict(int)
    for i in clothes:
        cloth_list[i[-1]]+=len(i)-1
    num_list=[i[1] for i in sorted(cloth_list.items(),key=lambda x:x[1], reverse=False)]
    print(num_list)
    if len(cloth_list)==1:
        return sum(cloth_list.values())
    else:
        return possibilities(num_list)

