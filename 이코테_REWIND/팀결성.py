# 팀 결성


n,m = map(int,input().split())

def Union(parent,n,m):
    a = find_parent(parent,n)
    b = find_parent(parent,m)

    if a<b : # 만약에 a보다 b가 크다면
        parent[b] = a # 더 작은수가 부모가 됩니다!
    else:
        parent[a] =b



def find_parent(parent,x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]


parent = [0 for _ in range(n+1)]

for i in range(n+1):
    parent[i] = i
for _ in range(m):
    classifier,a,b = map(int,input().split())
    if classifier == 0:
        # union 연산 수행
        Union(parent,a,b)
    elif classifier == 1:
        # 같은팀 여부확인
        if find_parent(parent,a) == find_parent(parent,b):
            print('yes')
        else:
            print('no')

