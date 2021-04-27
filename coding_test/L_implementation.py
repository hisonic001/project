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

n = 5
plans = ["R", "R", "R", "U", "D", "D"]
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ["L", "R", "U", "D"]
for plan in plans:
    print(plan)
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    print(nx, ny)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny
