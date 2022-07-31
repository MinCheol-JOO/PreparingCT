n,m,k,x = map(int,input().split())
graph = [[]for _ in range(m+1)]
tmp = []
for _ in range(m):
    a = list(map(int,input().split()))
    tmp.append(a)

for i in tmp:
    graph[i[0]].append(i[1])


# bfs로 탐색 시작
from collections import deque
import math
distance_list = [math.inf for _ in range(n+1)] # index는 해당 노드의 값 # value는 해당 노드까지의 거리
q = deque()
q.append(x)
distance_list[x]=0

distance = 0
while q:
    start = q.popleft()
    distance +=1
    for i in graph[start]:
        if distance_list[i]>distance:
            distance_list[i]=distance
        q.append(i)
print(distance_list)


for idx,i in enumerate(distance_list):
    if i == k:
        print(idx)