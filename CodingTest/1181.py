amount = int(input())

axis = []
for i in range(amount):
    x = input()
    axis.append(x)

axis = list(set(axis))

axis.sort(key = lambda x : (len(x),x))
# sort는 기본적으로, ascii code 순서로 정렬을 이루낟.



# x[1]의 값을 기준으로 정렬한다
# 그다음 두번쨰 값을 기준으로 정렬한다.

# axis.sort(key = lambda x : (x[1],-x[0]))
# 이렇게 하면 두번째를 기준으로 정렬할때 내림차순으로 정렬할수 있다.

#정렬을 원하는 함수
# 

for i in axis:
    print(i)



