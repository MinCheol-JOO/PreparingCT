# 미로 크기 입력받기. n은 row의 수, m은 column의 수
n,m = map(int,input().split())

# 그래프 입력받기
graph = []

# 1,1을 만들어주기 위해서
for _ in range(n):
    temp = list(map(int,input()))
    graph.append(temp)

print(graph)


# 미로는 반드시 탈출할 수 있고, 
# 탈출하기 위해 움직여야하는 최소칸의 개수를 구하여라

from collections import deque
# bfs로 풀기
def bfs(x,y):
    # 먼저, 큐를 생성합니다
    queue = deque()
    
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    # 큐에다가 m,n을 튜플형태로 넣어줍니다.
    # bfs는 큐에다가 넣고, 연결된 모든 노드를 찾아서 search하는 알고리즘이니까,
    # 모든 노드는 큐에 넣고 빼는 형식으로 작동되어야 합니다.
    queue.append((x,y))
    while queue:
        new_x,new_y = queue.popleft()

        for i in dir:
            nx = new_x+i[0]
            ny = new_y+i[1]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
        
            if graph[nx][ny]==1:
                # 비교를 할때 전체 column,row의 개수를 뜻하는 m,n의 변수값과
                # 각 location의 component x,y의 값을 헷갈리게 변수지정해놔서
                # 여기에 대한 디버깅을 진행하는데 있어서 시간을 많이 사용하였음
                graph[nx][ny]= graph[new_x][new_y]+1
                # 안되었던 이유
                # x를 자꾸 꺼내서 넣어줬으니, 전혀 엉뚱한 값이 튀어나왔음.

                queue.append((nx,ny))
    # return graph[n-1][m-1]
    return graph

print(bfs(0,0))

            

