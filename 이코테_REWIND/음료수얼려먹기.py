from collections import deque

graph = []
n,m = map(int,input().split())
# 음료수 얼려먹기 생성
for _ in range(n):
    a = list(map(int,input()))
    graph.append(a)

# dfs 진행
def dfs(x,y):
    # 만약 x,y가 1이 아니라면
    if x<0 or x>=n or y<0 or y>=m:
        return False


    if graph[x][y] == 0:
        graph[x][y]=1
        
        bfs(x-1,y)
        bfs(x+1,y)
        bfs(x,y-1)
        bfs(x,y+1)
        return True

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt+=1
print(cnt)


# # bfs로 풀기
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))

#     if graph[x][y] == 1:
#         return False
    
#     while queue:
#         x,y = queue.popleft()
#         graph[x][y] = 1
     
#         for i in range(4): # nx의 값과 ny의 값이 모두 0이 아니고, graph에서 방문하지 않았을경우에
#             ny = y+dy[i]
#             nx = x+dx[i]
#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
#             # if graph[nx][ny] == 0 and 0 <= nx < n and 0 <= ny < m :
#                 queue.append((nx,ny))

#     return True


# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if bfs(i,j) == True:
#             cnt+=1
# print(cnt)
