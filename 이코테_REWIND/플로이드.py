# 플로이드
n= int(input())
m = int(input())
graph = [[]for _  in range(n+1)]
for _ in range(m):
    a= list(map(int,input().split()))
    graph[a[0]].append((a[1],a[2]))


import math
import heapq
def dijkstra(start,end):
    distance = [math.inf for _ in range(n+1)]
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        distance_comp,now = heapq.heappop(q)
        # 현재 알고 있는값이 지금 꺼낸 최솟값보다 작으면 스킵
        if distance[now] < distance_comp:
            continue
        # graph 해당 node에서
        for i in graph[now]:
            cost = distance_comp+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))

    # print(distance)

    if distance[end] == math.inf:
        return 0
    return distance[end]

    


for i in range(1,n+1):
    for j in range(1,n+1):
        print(dijkstra(i,j),end = ' ')

    print()


