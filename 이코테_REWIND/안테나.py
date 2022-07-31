# # 안테나
# n= int(input())
# loc = list(map(int,input().split()))

# all_distance = [-1 for _ in range(max(loc))]
# for i in range(max(loc)): # 안테나 설치한 곳
#     distance = 0
#     for j in loc:
#         distance+=abs(j-i)
#     all_distance[i] = distance


# print(all_distance.index(min(all_distance)))

# 시간초과

# 답안 참고해서 다시 풀어봄

# # 안테나
n= int(input())
loc = list(map(int,input().split()))
loc = sorted(loc)
print(loc[(len(loc)-1)//2])