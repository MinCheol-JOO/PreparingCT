# 개미전사
# 22.07.06 2252

n = int(input())
food_storage = list(map(int,input().split()))

# 바텀업 방식
d = [0]* 100
d[0] = food_storage[0]
d[1] = max(food_storage[0],food_storage[1])
for i in range(2,n):
    d[i] = max(d[i-2]+food_storage[i],d[i-1])

print(d[n-1])

# 탑다운 방식
d = [0 for _ in range(1000)]
