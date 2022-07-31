# 금광
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    num_list = list(map(int,input().split()))

    i_cnt = 0
    geumgwang = []
    for i in range(n):
        geumgwang.append(num_list[i_cnt:i_cnt+m])
        i_cnt +=m
    



    # 다이나믹 프로그래밍 수행
    for j in range(1,m):
        for i in range(n):
            if i == 0 :
                left_up = 0
            else:
                left_up = geumgwang[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down=geumgwang[i+1][j-1]
            left = geumgwang[i][j-1]
            geumgwang[i][j]= geumgwang[i][j] + max(left_up,left_down,left)
    print(geumgwang)

