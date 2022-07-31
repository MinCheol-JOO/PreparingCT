def solution(n, weak, dist):
    dist.sort(reverse= True)
    count = 0
    W,F = len(weak), len(dist)
    len_weak = len(weak)
    repair_lst = [()]
     
    for can_move in dist: # 움직일 수 있는 범위
        repairs = []
        count +=1
        
        # 수리 가능한 지점을 찾습니다
        for i,wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]] # i의 행부터 시작하고, 시작점 기준의 끝 포인트를 저장한다
            can = [end%n for end in ends if end-start<=can_move] #만약 end-start가 can_move(움직일수 있는 거리)보다 적을 경우 end%n을 연산한 리스트를 만든다
            repairs.append(set(can)) # 나머지 연산으로 인해 겹쳐 있는 숫자가 있을수 있으므로 이에 대해서 set 연산을 수행합니다
            # 이렇게 되면 repairs 안에는 각 weak마다 점검할수 있는 취약점들이 보이게 됩니다.
        
        # print(repairs)
        # 수리가 가능한 경우를 탐색합니다.
        cand = set()
        for r in repairs:
            for x in repair_lst:
                # print(x)
                new = r| set(x) # 합집합 연산입니다. 이를 통해서 만약에 r에 x값이 없으면 r이 그대로 new값에 들어갈 수 있어요
                # print(new)
                if len(new) == W:
                    return count
                cand.add(tuple(new))
                # print(cand)
        repair_lst = cand
    
    
    return -1


    # 파이썬
from itertools import permutations
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]  # 선형으로

    for i, start in enumerate(weak):
        for friends in permutations(dist):  # 순열 이용
            count = 1
            position = start
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[i+L-1]:
                    count += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    position = [w for w in weak_point[i+1:i+L]
                                if w > position][0]
                else:  # 끝 포인트까지 도달
                    cand.append(count)
                    break

    return min(cand) if cand else -1