count = int(input())
from pickle import TRUE


# count = 3;
for i in range(count):
    x,y = map(int,input().split());
    d = y-x
    n = 0; # 반복 횟수를 합친 친구들
while True: 
    if d <= n*(n+1):
        break
        n += 1

if d <= n**2: 
    print(n*2-1) #총 이동 거리가 n의 제곱보다 클 때 
else:
    print(n*2)


# count = 10
# for _ in range(count):
#     x,y = map(int, input().split())
#     d= y-x
#     move= 1 # 해당 움직이는 값
#     move_plus = 0; # 움직이는 거리
#     count= 0; # 몇번쨰 반복하는지
#     while(move_plus<d):
#         count+=1; 
#         move_plus += move;
#         if count%2==0:
#             move+=1;
#     print(count)
    