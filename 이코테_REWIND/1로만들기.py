# 1로 만들기
num1 = int(input())
# 점화식 : 이건 서로 나눠서 생각해봐야 하는데,
# greedy algorithm이라는 각 상황에서의 최적해가
# 반드시 마지막에 최적해를 보장하지 않는 반증이 된다.
# 여기에서는 DP를 통해 a,b,c,d를 모두 따져보면서 최적해를 구하는 식으로 엔지니어링 되어야한다.

# 바텀업 방식
# d = [0 for _ in range(27)]

# for i in range(2,num+1):
#     d[i] = d[i-1]+1
#     if i%2 == 0:
#         d[i] = min(d[i],d[i//2]+1)
#     elif i%3 == 0:
#         d[i] = min(d[i],d[i//3]+1)
#     elif i%5 == 0:
#         d[i] = min(d[i], d[i//5]+1)

# print(d)

#탑다운
d = [0 for _ in range(30001)]
def num(x):
    # 정수 1일때는 0번 계산
    if x==1:
        return 0 
    
    # 연산 횟수가 0이 아닐경우
    if d[x] != 0:
        return d[x]

    # 나누어 떨어지지 않았을 때, 최솟값이 되지 않도록 높은 값 설정
    five = three = two = 99999

    if x % 5 ==0:
        five = num(x//5)
    if x%3 == 0:
        three = num(x//3)
    if x%2 == 0:
        two = num(x//2)


    d[x] = min(five,three,two,num(x-1))+1
    return d[x]

print(num(num1))