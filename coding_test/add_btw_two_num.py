a = 3
b = 156165
answer = 0
if b > a:
    nums = [i for i in range(a, b + 1)]
else:
    nums = [i for i in range(b, a + 1)]

answer = sum(nums)

print(answer)