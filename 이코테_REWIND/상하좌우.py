# 상하좌우. 이코테 111쪽.
space = int(input())
move_likeit = list(input().split())

x = 1
y = 1

def move(x,y,howtomove,height):
    if howtomove == 'R':
        dx = x+1
        dy = y
    elif howtomove == 'U':
        dy = y-1
        dx = x
    elif howtomove == 'D':
        dy = y+1
        dx = x
    elif howtomove == 'L':
        dx = x-1
        dy = y

    if dx<1 or dx>height or dy<1 or dy>height:
        return x,y


    return dx,dy
    



for i in range(len(move_likeit)):
    x,y = move(x,y,move_likeit[i],space)


print(y+1,x+1) 