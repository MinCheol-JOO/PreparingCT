# 성적이 낮은 순서대로 학생출력하기
n = int(input())

array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array,key = lambda x : x[1])

for i in array:
    print(i[0],end= ' ')