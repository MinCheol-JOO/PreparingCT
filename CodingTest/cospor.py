# 다음과 같이 import를 사용할 수 있습니다.
import math

def solution(garden):
    answer = 0;
    dx = [1,0,-1,0]#동남서북
    dy = [0,-1,0,1]
    next = []

    for i in range(len(garden)):
        for j in range(len(garden)):
            if garden[i][j]==1:
                next.append([i,j]) # 현재 위치를 알려준다
        
        for i in next: # next에 있는 모든 친구들을 뜻함 [1,2] 하나씩들을 뜻하겠죠?
            for j in range(len(garden)):
                x= dx[j]+i[0]
                y =dy[j]+i[1]

                if (x>=0 and x<len(garden)) and (y>=0 and y<len(garden)):
                    garden[x][y]=1

        answer +=1
    return answer-1

        

        

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)
# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

# garden2 = [[1, 1], [1, 1]]
# ret2 = solution(garden2)

# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret2, "입니다.")