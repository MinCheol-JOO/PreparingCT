n,m,k = map(int,input().split())
int_list = list(map(int,input().split()))
# 그리디 실전문제 2
# 처음에 n,m,k를 입력받고

int_list.sort()
max_num = int_list[-1]
second_num = int_list[-2]

summer = 0
while m>0:
    for i in range(k):
        summer+=max_num
        m-=1
    
    if m>0:
        summer+=second_num
        m-=1


print(summer)
