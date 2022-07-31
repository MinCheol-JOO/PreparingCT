def solution(arr):
    answer = 0 
    answerpz = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            answer +=1
            answerpz.append(answer)
        if arr[i] >= arr[i+1]:
            answer =0
        print(answerpz)
    answer = max(answerpz)+1
    return answer

arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")