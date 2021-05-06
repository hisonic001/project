# # import sys
# # input = sys.stdin.readline
# INF = int(1e9)
#
# n,m = map(int,input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# visit = [False] * (n+1)
# distance = [INF] * (n+1)
#
# #모든 간선 정보 입력
# for _ in range(m):
#     a,b,cost = map(int,input().split())
#     graph[a].append((b,cost))
#
# #방문하지 않은 노드 중에서 가장 최단거리 짧은 노드를 반환
# def get_smallest_node:
#     min_value = INF
#     index = 0 #가장 최단거리가 짧은 노드
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[i]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# dijkstra(start)
#
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INFINITE")
#     else:
#         print(distance[i])
# --------------------------------------------
#  힙 사용하기
# import heapq
#
# def heapsort(iterable):
#     h = []
#     result = []
#     for value in iterable:
#         heapq.heappush(h,-value)
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)
# ---------------------------------------------
import heapq

graph = {
'a':{'b':8,'c':1,'d':2},
'b':{},
'c':{'b':5,'d':2},
'd':{'e':3,'f':5},
'e':{'f':1,},
'f':{'a':5}
}

import heapq

def dijkstra(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    que = []
    heapq.heappush(que, (distances[start], start))

    while que:
        current_distance, current_destination = heapq.heappop(que)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(que,[distance,new_destination])
    return distances

print(dijkstra(graph,'a'))
