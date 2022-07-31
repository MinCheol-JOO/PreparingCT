# cos pro 7번
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def find(parent, u):
	if u == parent[u]:
		return u
	parent[u] = find(parent,parent[u])
    # parent안에 있는 parent값을 가지고 와서 parent값이 얼마인지 알려준다
	return parent[u]

def merge(parent, u, v):
	u = find(parent, u)
	v = find(parent, v)
	if u == v:
		return True
	else:
		return False

def solution(n, connections):
	answer = 0
	parent = connections[0]
	for i, connection in enumerate(connections):
		if merge(parent, connection[0], connection[1]):
			answer = i + 1
			break
	return answer


n=3
connections = [[1,2],[1,3],[2,3]]
ret = solution(n,connections)

print(ret)