amount = int(input())

axis = []
for i in range(amount):
    x,y = map(int,input().split())
    axis.append([x,y])

axis.sort(key = lambda x : (x[1],x[0]))
# x[1]의 값을 기준으로 정렬한다
# 그다음 두번쨰 값을 기준으로 정렬한다.

# axis.sort(key = lambda x : (x[1],-x[0]))
# 이렇게 하면 두번째를 기준으로 정렬할때 내림차순으로 정렬할수 있다.

#정렬을 원하는 함수
# 

for i in axis:
    print(i[0],i[1])



