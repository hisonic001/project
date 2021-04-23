s = "abcdd"
def solution(s):
    split = len(s) // 2
    rest = len(s) % 2
    if rest == 1:
        print (s[split])
    elif rest == 0:
        print (s[split-1:split+1])
solution(s)