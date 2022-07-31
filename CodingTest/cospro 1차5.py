

def makeBoard(n):
	dx = [1,0,-1,0]
	dy = [0,-1,0,1]
	board = [[[0]*n]*n]
	#3x3의 경우 3번 한번 움직이고, 2번, 2번, 1번, 1번.. 이런식으로 움직인다는 것을 기억해보자
	x=0;
	y=0;
	i = 0
	j = 0 # y축 움직일 array idx
	value = 1 ; # 현재 넣어야할 값
	while(n>0): # 전부 다 돌떄까지
		dx_a = dx[i%4] # 지금 움직이는 거리
		dy_a = dy[i%4]
		for k in range(n-1): # 한 줄씩 업데이트!
			board[y][x]=value; # 1 넣어주고
			x +=dx_a # 
			y+=dy_a
			value +=1
			print(board)
		i+=1
		j+=1
		if n  % 2 == 0:
			n-=1; # 몇 번 움직여야 할지를 업데이트 해줌

print(makeBoard(3))