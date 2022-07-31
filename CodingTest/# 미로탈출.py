# 미로탈출
from collections import deque


n,m = map(int,input().split())


maze = []
for _ in range(n):
    maze.append(list(map(int,input())))

# 동빈이의 위치는 (1,1)이다
# 만약에 0에 괴물이 있으면 무시해야한다

# 옮기는 dir 지정
x_loc = [1,0,-1,0]
y_loc = [0,-1,0,1]

x = 0 # 원래는 1,1에서 시작해야 하지만 0,0에서 실행하는 것으로 지정하엿다
y = 0 

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4):

            nx = x+x_loc[i]
            ny = y+y_loc[i]
            # 
            if nx>=n or nx<0 or ny>=m or ny<0 :
                continue
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx,ny))

    return maze[n-1][m-1]


print(bfs(0,0))
    