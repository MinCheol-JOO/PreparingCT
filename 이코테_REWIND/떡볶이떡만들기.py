# 떡볶이 떡 만들기
# 떡의 개수 n, 요청한 떡의 길이 m
# m,n = map(int,input().split())

# # 떡의 개별 높이
# tteok = list(map(int,input().split()))

# 높이가 10억보다 작거나 같은 양의 정수 또는 0이라고 했으니 반드시 이진탐색을 고려해야한다.
# 문제에서 말하는 것은 m보다 많은 양의 떡을 얻기 위해 절단기에 설정할 수 있는 최댓값을 산출하는 프로그램을 만드는 것이다

# idea
# tteok을 sorted 하여 중앙값으로 자를 크기를 잡았는데, 그게 산출되는 값이 크면, 자를 크기를 조금더 늘리고, 반대는 자를 크기를 줄인다!

n, m = map(int, input().split())
print(n,m)
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while(start <= end) :
  total = 0
  mid = (start+end) // 2
  for x in arr :
    if x > mid :
      total += x - mid
  
  if total < m :
    end = mid - 1
  else :
    result = mid
    start = mid + 1

print(result)