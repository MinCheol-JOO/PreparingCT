#볼링공 고르기

from itertools import combinations
n,m = map(int,input().split())
ball = list(map(int,input().split()))

ballings_set = combinations(balls,2)

count = 0
for i in ballings_set:
    if i[0] != i[1]:
        count+=1

print(count)