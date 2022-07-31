from itertools import combinations


# 치킨 배달
n,m = map(int,input().split())
chicken,house = [],[]

# 2를 전부 다 빼보고 하나씩 넣어보자!

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for hx,hy in house:
        # 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))

        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)
