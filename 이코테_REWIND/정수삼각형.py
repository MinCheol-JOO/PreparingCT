n = int(input())
array = []
for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)

d = [0 for _ in range(500+1)]
d[1] = array[0][0]
for i in range(1,n): # row의 갯수
    for j in range(i+1): # column의 갯수
        if j-1<0:
            left = 0
        else:
            left = array[i-1][j-1]
        if j+1>i:
            right = 0
        else:
            right = array[i-1][j]

        array[i][j] = array[i][j]+ max(left,right)

print(max(array[n-1]))