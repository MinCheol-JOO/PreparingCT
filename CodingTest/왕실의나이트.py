str1 = 'a1'
nx = ord(str1[0])-ord('a')
ny = ord(str1[1])-ord('1')

dx_1 = [2,2,-2.-2]
dy_1 = [1,-1,1,-1]

dx_2 = [1,1,-1,-1]
cnt = 0
dy_2 = [2,-2,2,-2]

tempx = nx
tempy = ny
for i in range(len(dx_1)):
    tempx = nx
    tempy = ny
    tempx+=dx_1[i]
    if tempx<0 or tempx>7:
        continue;
    tempy+=dy_1[i]
    if tempy<0 or tempy>7:
        continue;
    cnt+=1

for i in range(len(dx_1)):
    tempx = nx
    tempy = ny
    tempx+=dx_2[i]
    if tempx<0 or tempx>7:
        continue;
    tempy+=dy_2[i]
    if tempy<0 or tempy>7:
        continue;
    cnt+=1
print(cnt)
    
