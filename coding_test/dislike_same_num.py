arr = [1, 1, 3, 3, 0, 1, 1]
answer = []
num = 0
for i in arr:
    if num != i:
        num = i
        answer.append(num)


print(answer)
