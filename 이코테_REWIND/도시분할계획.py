# 도시 분할 계획
n,m = map(int,input().split())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    x = find_parent(parent,a)
    y = find_parent(parent,b)

    if x<y:
        parent[y]=x
    else:
        parent[x]=y

parent = [0 for _ in range(n+2)]

# 자기자신으로 초기화한다.
for i in range(1,n+1):
    parent[i]=i

def kruskal(edges,parent):
    result = 0
    last = 0
    for edge in edges:
        cost,a,b = edge
        # 싸이클이 존재하지 않을경우
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result+=cost
            # 두개의 분리된 마을로 만들기 위해서는 가장 큰 간선을 지우기만 하면 두개의 최소 MST가 만들어진다
            last = cost

    return result-last


edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b)) # c를 기준으로 정렬하기 위해

edges.sort()

print(kruskal(edges,parent))