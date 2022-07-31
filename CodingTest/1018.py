N, M = map(int, input().split())

original = []

for _ in range(N):
    original.append(input())

count= []

for a in range(N-7):
    for b in range(N-7):
        index1 = 0 # w로시작할경우
        index2 = 0# b로 시작할경우
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if original[i][j] != 'W': # 'w'로 시작할경우 바뀐 체스판의 갯수를 세기 위함
                        index1 +=1
                    if original[i][j] != 'B':
                        index2+=1
                else:
                    if original[i][j] != 'B':
                        index1+=1
                    if original[i][j] != 'W':
                        index2+=1
        count.append(min(index1,index2))
print(min(count))
