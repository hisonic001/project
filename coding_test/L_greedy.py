# n = 3850
# count = 0
# n500 = n // 500
# n100 = (n - n500 * 500) // 100
# n50 = (n - n500 * 500 - n100 * 100) // 50
# n10 = (n - n500 * 500 - n100 * 100 - n50 * 50) // 10

# total = sum([n500, n100, n50, n10])
# print(total)

# list = [500, 100, 50, 10]
# for coin in list:
#     count += n // coin
#     n = n % coin
# print(count)

# ------------------------------------
# n을 k로 나누거나 -1 해주기 1이 될 때 까지
# n = 25
# k = 3
# count = 0

# while n != 1:
#     if n % k != 0:
#         n -= 1
#         count += 1
#     else:
#         n //= k
#         count += 1
# -------------------------------------
#
# 더하거나 곱하거나 큰수 만들기
# s = "567"
# ans = 0
# for i in list(map(int, s)):
#     if ans * i > ans + i:
#         ans *= i
#     else:
#         ans += i
# print(ans)

# -------------------------------------------

#모험가 공포도에 따라 몇번이나 그룹으로 보낼 수 있는가?

fear = "2 3 1 2 1 2 1 1 1 1"
count = 0
before = 0
fear = list(sorted(map(int, fear.split(" ")), reverse=True))
n = len(fear)
print(fear)
for i in range(n):
    if before > 0:
        before -= 1
        continue
    if n >= fear[i]:
        n -= fear[i]
        count += 1
        if fear[i] > 1:
            before = fear[i]
        print(n)

print("\n", count)
