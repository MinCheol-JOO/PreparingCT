# 뱀
n = int(input())
k = int(input())

dir_change = [] # 그때 몇초에 어디로 변하는지 (시간, 방향)
apple_location =[]

# 사과의 위치
for _ in range(k):
    c,d = map(int,input().split())
    apple_location.append((c,d))

# 방향 정보
L = int(input())
for _ in range(L):
    c,d = input().split()
    dir_change.append((int(c),d))

# 빠른 순서대로 오름차순 정렬하기 위해서
dir_change = sorted(dir_change,key = lambda x : x[0])

graph = [[0 for _ in range(n+1)] for _ in range(n+1)] #0~n-1의 행 및 열만이 존재한다
for i in apple_location:
    graph[i[0]][i[1]] = 1


snake_x =1
snake_y=1
snake_present = [[snake_x,snake_y]] # 현재 스네이크가 있는 자리들을 확인

cnt=0

def direction(dir_change,present_dir):
    #동,
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    # 질문 : 이게 우측 상단으로 나오니까 위로 이렇게 올리는 방식말고는 잘 모르겠더라구요.. 
    # 그러니까, 
    for idx,i in enumerate(dir):
        if present_dir == i:
            present_idx = idx
            break
    if dir_change[1] == 'D':
        return dir[(idx+1)%4]
    elif dir_change[1] == 'L':
        return dir[(idx-1)%4]

# 우하좌상 제어
present_dir = (0,1)
while True: # snake_x,snake_y가 벽에 닿지 않을 경우만 순회하도록 설계
    # 해당시간에 방향을 바꾸어야 한다면
    if dir_change:
        if dir_change[0][0] == cnt:
            present_dir= direction(dir_change[0],present_dir)
            dir_change.pop(0)

    cnt+=1
    # 스네이크 이동
    nx = snake_x+present_dir[0]
    ny = snake_y+present_dir[1]
    
    # print([ny,nx])
    if nx<1 or nx>n or ny>n or ny<1 or [nx,ny] in snake_present:
        break

    # 해당 그래프에 사과가 있을 경우에는
    if graph[nx][ny] == 0 :
        snake_present.pop(0)
    snake_present.append([nx,ny])
    # print(snake_present)
    snake_x = nx
    snake_y = ny

    

print(cnt)
