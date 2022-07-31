# 게임 개발
n,m = map(int,input().split())
x_loc,y_loc,present_dir = map(int,input().split())
graph = []
for i in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

dir = [(0,1),(1,0),(0,-1),(-1,0)]

visited = [[0 for _ in range(m)]for _ in range(n)]
visited[x_loc][y_loc]=1
cnt = 0
while True:
    # 현재 위치에서 현재방향을 기준으로 왼쪽방향부터 갈 곳 정하기
    if cnt>4:
        x_temp = x_loc-dir[present_dir][0]
        y_temp= y_loc-dir[present_dir][1]
        if graph[x_temp][y_temp] == 0:
            break
        else:
            x_loc = x_temp
            y_loc = y_temp
            break

    present_dir = (present_dir+3)%4
    cnt+=1

    # 캐릭터의 왼쪽 방향에 가보지 않은 칸이 있다면,
    dx = x_loc+dir[present_dir][0]
    dy = y_loc+dir[present_dir][1]

    if visited[dx][dy]==0 and graph[dx][dy]==0:
        visited[dx][dy]=1
        x_loc = dx
        y_loc = dy
        cnt=0


cnt_all =0
for i in visited:
    cnt_all+= sum(i)

print(cnt_all)