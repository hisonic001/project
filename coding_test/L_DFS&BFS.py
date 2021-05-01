
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y -+1)
        return True
    return False

n,m = 2,2
model = [['00110'],['00011'],['11111'],['000000']]
graph = []
result = 0
for i in range(n):
    graph.append(list(map(int,model[i][0])))

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
