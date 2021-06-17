from collections import deque
def solution(priorities, location):
    a=1
    out=[]
    outnum=[]
    num=[i for i in range(len(priorities))]
    num.reverse()
    priorities.reverse()
    print(priorities)
    while len(priorities)>=1:
        print(a)
        if len(priorities)==1:
            out.append(priorities.pop())
            outnum.append(num.pop())
            print(priorities,out,"lll",num,outnum)
            break
        if priorities[-1]<max(priorities[:-1]):
            low = priorities.pop()
            priorities.insert(0,low)
            low = num.pop()
            num.insert(0,low)
            print(priorities,out,"lll",num,outnum)
            a+=1
            continue
        if priorities[-1]>=max(priorities[:-1]):
            out.append(priorities.pop())
            outnum.append(num.pop())
            print(priorities,out,"lll",num,outnum)
            a+=1
    out+=priorities
    outnum+=num
    return outnum.index(location)+1

priorities=[2,1,3,2]
location=2

print(solution(priorities,location))