s = "try hello world"


def solution(s):
    num = -1
    answer = ""
    for i in s:
        if i != " ":
            num += 1
        if i == " ":
            num = -1
            answer += i
            continue
        if num % 2 == 0:
            answer += i.upper()
        if num % 2 == 1:
            answer += i.lower()
    print(answer)


solution(s)
# def solution(s):
#     changed = ""
#     changed += s[0].upper()
#     for i in range(1, len(s)):
#         if s[i] == " ":
#             changed += s[i]
#             continue
#         if changed[i - 1].isupper():
#             changed += s[i]
#         elif changed[i - 1].islower():
#             changed += s[i].upper()
#         elif changed[i - 1] == " ":
#             changed += s[i].upper()
#     print(changed)


# solution(s)
