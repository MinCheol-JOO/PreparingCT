# 그리디 실전문제 4
n,k = map(int,input().split())
cnt =0
while n>1: # 1이 될때까지 
    if n%k == 0: # 나머지가 0이면 나누어 떨어지는것
        n//=k
    else:# 그렇지 않으면 -1을 진행한다
        n-=1
    cnt+=1

print(cnt)