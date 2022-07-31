# 미래 도시
import math
# 전체 회사의 개수
n,m = map(int,input().split())
graph = []
for _ in range(m):
    a = list(map(int,input().split()))
    graph.append((a[0],a[1]))
    graph.append((a[1],a[0]))
x,k = map(int,input().split())
# 플로이드 워셜 알고리즘 수행
def floyd_warshall(company_num,graph): # companynum : 전체 회사의 개수
    weights = [[math.inf for _ in range(company_num+1)]for _ in range(company_num+1)]
    for i in range(1,company_num+1):
        for j in range(1,company_num+1):
            if i == j:
                weights[i][j] =0

    while graph:
        a,b = graph.pop()
        weights[a][b] =1

    for i in range(1,company_num+1):
        for j in range(1,company_num+1):
            for k in range(1,company_num+1):
                weights[i][k] = min(weights[i][k],weights[i][j]+weights[j][k])

    return weights

the_weights = floyd_warshall(n,graph)
distance =the_weights[1][k]+the_weights[k][x]
if distance != math.inf:
    print(distance)
else:
    print(-1)











