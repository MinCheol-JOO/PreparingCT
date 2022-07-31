# 전보

n,m,c = map(int,input().split())
# n의 범위가 30000개로 굉장히 많기 떄문에,
# dijkstra를 사용하여 구현하는 것이 요구됨

connectivity = [[]for _ in range(n+1)] # 어떻게 그래프가 연결되어 있는지
for _ in range(m):
    x,y,z = map(int,input().split())
    connectivity[x].append((y,z)) #

import math
distance = [math.inf for _ in range(n+1)] # 1에서 부터 n까지를 사용하고, 0 vertex는 사용하지 않는다

import heapq
def dijkstra(start): # 여기에서는 graph를 산출하고, inf가 아닌 애들중에 가장 큰 값을 산출하고,
    # 또한 그 개수를 세도록 만들어야 한다
    q = []
    heapq.heappush(q,(0,start))
    # heap에서는 앞에있는것을 기준으로 heap을 정렬하기 때문에 이렇게 만들어야한다,
    distance[start] = 0
    while q:
        distance_comp,now = heapq.heappop(q)
        # heap에서 꺼낸뒤
        # 최단거리에 해당하는 노드에 대한 정보를 꺼낸다
        if distance[now]<distance_comp:
            continue # 스킵
        # connectivity 그래프에서 연결된 인접된 노드를 확인한다
        for i in connectivity[now]:
            cost = distance_comp+i[1]
            if  cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
cnt = 0
max = -1
print(distance)
for i in range(1,len(distance)):
    if distance[i] != math.inf:
        cnt+=1
    if max<distance[i]:
        max = distance[i]
print(cnt-1,end=' ') # 자기자신을 뺴야합니다!
print(max)

