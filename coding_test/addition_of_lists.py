a = [[1], [2]]
b = [[3], [4]]


c = [[0] * len(a[0]) for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

print(c)

## zip의 활용
num = [1, 2, 3, 4]
name = ["kim", "jun", "cho", "lee"]

li = [[i, j] for i, j in zip(num, name)]
print(li)