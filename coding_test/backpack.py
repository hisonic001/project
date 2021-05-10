# nk = "4 7"
# n, k = map(int, nk.split())
# wv = ["6 13", "4 8", "3 6", "5 12"]
# pack_list = []
# dp = [[0] * (k + 1) for _ in range(n)]

# for i in range(n):
#     w, v = map(int, wv[i].split())
#     pack_list.append((w, v))
#     print(w, v)

# for i in range(n):
#     if i == 0:
#         for j in range(k + 1):
#             if j >= pack_list[i][0]:
#                 dp[i][j] = pack_list[i][1]
#         continue
#     for j in range(k + 1):
#         if j < pack_list[i][0]:
#             dp[i][j] = dp[i - 1][j]
#         if j >= pack_list[i][0]:
#             dp[i][j] = max(
#                 dp[i - 1][j], pack_list[i][1] + dp[i - 1][j - pack_list[i][0]]
#             )
# print(dp[n - 1][k])


def backpack():
    n, k = map(int, input().split())
    pack_list = []
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        w, v = map(int, input().split())
        pack_list.append((w, v))
    for i in range(n):
        if i == 0:
            for j in range(k + 1):
                if j >= pack_list[i][0]:
                    dp[i][j] = pack_list[i][1]
            continue
        for j in range(k + 1):
            if j < pack_list[i][0]:
                dp[i][j] = dp[i - 1][j]
            if j >= pack_list[i][0]:
                dp[i][j] = max(
                    dp[i - 1][j], pack_list[i][1] + dp[i - 1][j - pack_list[i][0]]
                )
    print(dp[n - 1][k])


backpack()
