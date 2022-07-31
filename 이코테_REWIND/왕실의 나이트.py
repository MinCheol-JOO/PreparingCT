# 왕실의 나이트
# str_location = list(input())

# mover = [(-2,1), (-2,-1),(2,1),(2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]

# start_col = ord(str_location[0])-ord('a')+1 
# start_row = int(str_location[1])

# cnt=0

# for move_comp in mover:
#     next_row = start_row+move_comp[0]
#     next_col = start_col+ move_comp[1]

#     if next_row >=1 and next_row<=8 and next_col>=1 and next_col<=8:
#         cnt+=1

# print(cnt)

# 왕실의 나이트
knight = list(input())

mover = [(-2,1), (-2,-1),(2,1),(2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]

col = ['a','b','c','d','e','f','g','h']
row = [1,2,3,4,5,6,7,8]

cnt =0
for move in mover:
    # 인덱스를 찾아보고, 만약에 index가 포함되지 않았을 경우에는
    # print(knight[0])
    x = col.index(knight[0])
    y = row.index(int(knight[1]))

    dx = x+move[0]
    dy = y+move[1]

    print([dx,dy])
    if dx<=7 and dx>=0 and dy<=7 and dy>=0:
        cnt+=1

print(cnt)