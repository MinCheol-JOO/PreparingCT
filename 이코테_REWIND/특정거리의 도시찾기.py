# 도시의 개수, 도로의 개수, 거리정보, 출발도시 정보
city_count, path_count,for_distance,starting_point = map(int,input().split())
from_to = [[]for _ in range(city_count+1)]
for _ in range(path_count):
    temp = list(map(int,input().split()))
    from_to[temp[0]].append(temp[1])


import collections
from collections import deque

def bfs(from_spot,cost):
    # 시작부터 끝까지의 점중에서 해당 cost가 나오는 점까지의 거리가 산출되는 점을 찾아서 return 한다.
    queue= deque()

    distance = [-1 for _ in range(city_count+1)]
    distance[from_spot] =0
    cnt = 0
    queue.append(from_spot)
    while queue:
        to_spot = queue.popleft()
        for next_node in from_to[to_spot]:
            if distance[next_node] == -1:
                distance[next_node] = distance[to_spot]+1
                queue.append(next_node)

    check = False
    for i in range(1,city_count+1):
        if distance[i] == cost:
            return i
            check = True

    if check == False:
        return -1


print(bfs(starting_point,for_distance))