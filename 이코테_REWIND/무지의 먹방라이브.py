# 실패코드

import math
def solution(food_times, k):
    answer = 0
    size_food = len(food_times)
    step = math.inf
    for i in range(k+1): # k시간동안 돌아야함
    # 테스트케이스에서는 하나만 될경우를 가정해서 이렇게 코드를 짤수 있지만,
    # 만약에 그렇지 않았을 경우에는 이렇게 짜면 2개 이상이 정확한 시간 측정이 어려움. (굳이 이걸 쓰려면 -> While을 써야함)
        step = i%size_food
        if food_times[step]<1:
            continue
        food_times[step]-=1
        print(i,step,food_times)
    
    cnt = 0
    while food_times[step] == 0:
        if cnt>size_food:
            return -1
        step = (step+1)%size_food
        cnt+=1
    print(step)
    answer =step+1
        
    return answer

    # 실패하였음

from operator import itemgetter

def solution(food_times, k):
    foods = [] # 음식에 먹는데 필요한 시간
    n = len(food_times) # 음식의 개수
    for i in range(n):
        foods.append((food_times[i],i+1)) #  음식의 시간, 음식의 번호
        
    foods.sort()
    
    pretime = 0 # 이전음식과의 음식시간차
    for i, food in enumerate(foods):
        diff = food[0]-pretime
        if diff != 0 :
            spend = diff * n
            if spend <=k:
                k-=spend
                pretime = food[0]
            else:
                k%=n # 남은 음식중에서 차례대로 먹어야함
                sublist = sorted(foods[i:],key = itemgetter(1))
                return sublist[k][1]
        n-=1    
    return -1