amount = int(input())
from collections import Counter

a = []

for i in range(amount):
    x,y = map(int,input().split())
    a.append([x,y])

b= []
# 버블정렬 생각해볼까?
for i in range(amount):
    min_x = a[i][0]
    min_y = a[i][1]
    for j in range(i+1, amount):
        if min_x == a[j][0]:
            if min_y > a[j][1]:
                min_y = a[j][1]
                
                
        if min_x>a[j][0]:
            min_x = a[j][0]
            min_y = a[j][1]
    