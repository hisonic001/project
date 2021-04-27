# n = 5
# plan = "R R R U D D D R L L L L U D L R R R U D D R L U"
# list_plan = list(map(str, plan.split(" ")))
# print(list_plan)

# map = [[0 for col in range(n)] for low in range(n)]
# cor = 1
# low = 1

# for dir in plan:
#     if dir == "L":
#         cor -= 1
#         if cor < 1:
#             cor = 1
#     elif dir == "R":
#         cor += 1
#         if cor > 5:
#             cor = 5
#     elif dir == "U":
#         low -= 1
#         if low < 1:
#             low = 1
#     elif dir == "D":
#         low += 1
#         if low > 5:
#             low = 5
#     print(low, cor)
# --------------------------------------------------------------
# 좌표 이동하기
# n = 5
# plans = ["R", "R", "R", "U", "D", "D"]
# x, y = 1, 1

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# move_types = ["L", "R", "U", "D"]
# for plan in plans:
#     print(plan)
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     print(nx, ny)
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     x, y = nx, ny

# ------------------------------------------------------------------
# 시각문제 3이 몇개 있는가??  // 완전탐색 문제 모든 경우의 수를 고려
# N = 24  # ans = 11475
# h = [i for i in range(1, N + 2)]
# min = [i for i in range(1, 61)]
# sec = [i for i in range(1, 61)]
# count = 0

# for hour in h:
#     for minute in min:
#         for second in sec:
#             time = f"{hour}{minute}{second}"
#             if "3" in time:
#                 count += 1

# print(count)
# ---------------------------------------------------------------
# #왕실의 나이트 문제 해결
# x, y = 2, "c"
# eng = "a b c d e f g"
# list_of_y = list(map(str, eng.split(" ")))
# eng_y = dict(zip(list_of_y, [i for i in range(1, 11)]))
# y = eng_y[y]
# dx = [1, -1, -1, 1, -2, -2, 2, 2]
# dy = [-2, -2, 2, 2, 1, -1, 1, -1]
# move = ["LL", "LR", "RL", "RR", "UR", "UL", "DR", "DL"]
# answer = []

# for i in range(len(move)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     answer.append((nx, list_of_y[ny - 1]))
# print(answer)
# ---------------------------------------------------------------
# 문자열 재정렬
S = "KKACB0"  # "AJKDLSI412K4JSJ9D"  #
new_s = sorted(map(str, S))
num_list = list(map(str, "0123456789"))
numbers = []
alps = []
add_num = 0
count = 0
for num in new_s:
    if num in num_list:
        add_num += int(num)
        count += 1
    else:
        alps.append(num)
if count != 0:
    numbers.append(str(add_num))
print("".join(alps + numbers))
