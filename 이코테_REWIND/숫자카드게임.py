# 숫자쓰인 카드가 nxm형태로 놓여있고
# n과 m은 행의 개수 및 열의 개수를 의미한다
# 뽑고자 하는 카드가 포함되어있는 행을 선택하고
# 행에서 가장 숫자가 낮은 카드를 뽑는다
# 처음에 카드가 골라낸 행을 선택할 때 이후의 해당 행에서 가장 숫자가 낮은 카드를 뽑을 걸 고려하여 가장 높은 숫자의 카드를 뽑을수 있도록 한다

# 그리디 실전문제 3
# n,m = map(int,input().split())

# graph = []
# real_min_value = -1
# for _ in range(n):
#     temp = list(map(int,input().split()))
#     graph.append(temp)
#     min_value = min(temp)
#     # 만약에 min_value가 저장된 min 값보다 크면
#     # min_value에 현재 min값을 저장하고 현재의 행의 위치를 저장해준다
#     if real_min_value<min_value:
#         # 만약에 초기값 -1로 설정된 real_min_value가 각 행의 가장 작은 값보다 작다면,
#         # 더 큰 값을 real_min_value로 받도록 만들어준다.
#         real_min_value = min_value
#         row_loc = n


# print(real_min_value)

#     # 그렇지 않으면,
#     # 넘어간다


import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

ans = 0
for i in range(m):
    ans  += num[i]

print(ans)