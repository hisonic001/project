#
# #  얼음 얼려먹기 문제 // 얼음이 안 언곳을 재귀함수로 얼리고
# #  True값 주기 그래프를 벗어나거나 이미 언곳(1)이면 FALSE
# def dfs(x,y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# n,m = 4,5
# model = [['00110'],['00011'],['11111'],['000000']]
# graph = []
# result = 0
# for i in range(n):
#     graph.append(list(map(int,model[i][0])))
#
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result +=1
# print(result)

#  미로탈출문제
from collections import deque

n,m = 5,6
model = [['101010'],['111111'],['000001'],['111111'],['111111']]
graph = []

for i in range(n):
    graph.append(list(map(int,model[i][0])))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue
            if graph[nx][ny]==0:
                continue
            elif graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    print(graph)

bfs(0,0)
