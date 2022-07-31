# 1154 시작

def possible(answer):
    for x,y,stuff in answer : # x좌표, y좌표, 그리고 column,row 인지를 알려줌
        if stuff == 0 : # 기둥일 경우에는
            # 바닥위에 있거나, 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있어야 함
            # [x-1,y,1] -> 은 x-1에서 x까지 시작하는 보, [x,y,1]은 x에서 x+1까지 진행하는 보
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        
        elif stuff == 1:
            # 한쪽 끝부분이 기둥위에 있거나, 또는 양쪽 끝부분이 다른 보와 연결되어 있어야 한다
            if [x,y-1,0] in answer or [x+1,y-1,0]in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
        
    return True
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        elif operate == 1:
            answer.append([x,y,stuff])             
            if not possible(answer):
                answer.remove([x,y,stuff])                                   
    
    
    return sorted(answer)