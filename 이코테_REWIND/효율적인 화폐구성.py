# # 효율적인 화폐구성
# n,m = map(int,input().split())
# value = []
# for i in range(n):
#     a = int(input())
#     value.append(a)

# d = [10001 for _ in range(m+1)]

# # 이게 가능한 이유는 버텀업 형식으로 알고리즘을 설계할 경우에
# # j - value[i]에서 1을 더한식으로 알고리즘을 설계했으므로
# # min값을 취해주면 가장 최소한의 화폐개수를 출력할 수 있기 때문이다.


# d[0] = 0
# for i in range(n):
#     for j in range(value[i],m+1):
#         if d[j-value[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j],d[j-value[i]]+1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

# 효율적인 화폐구성

# 바텀업
# 바텀업은 결국 반복문을 통해 내부에서 구현하는 것
# 구현 방법이 비교적 어려운반면에, 공간적 복잡도에 대해 이점이 있음
# n,m = map(int,input().split())
# value = []
# for i in range(n):
#     a = int(input())
#     value.append(a)

# d =[10001 for _ in range(m+1)]

# d[0] = 0
# for i in range(n): # 0~n까지, 즉 화폐의 가짓수
#     for j in range(value[i], m+1): # value[i]부터 m까지의 모든 값을 흝는 느낌
#         if d[j-value[i]] != 10001:
#             d[j] = min(d[j],d[j-value[i]]+1) # d[j]가 이미 계산되었을 경우와 해당 값을 뺀 index에서 바로 1을 더했을 경우의 값과 비교를 진행합니다.
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])


# 탑다운
# 탐다운은 점화식을 통해 재귀적으로 풀수 있음
n,m = map(int,input().split())
array = [0]*10001
value = []
for i in range(n):
    a = int(input())
    value.append(a)
    array[a] = 1

def find(num):
    if num<0:
        return 10001
    count = 10001 # default, 원래의 값이 10001로 초기화
    if array[num] != 0:
        return array[num]
    for i in value:
        if find(num-i)<count: # 현재의 count 값이 find 전번 값보다 작다면
            count = find(num-i)

    array[num] =count+1
    return array[num]

print(find(m) if find(m)<10001 else -1)