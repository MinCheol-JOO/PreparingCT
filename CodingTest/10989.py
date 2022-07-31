import sys
n = int(sys.stdin.readline())
a = 10001
num_list = [0]*a

for _ in range(n):
    num_list[int(sys.stdin.readline())]  += 1
    # 인덱스에 해당하는 곳에 1을 넣어준다
    # 즉 , 9가 입력되면
    # num_list[9] =1이 되는것

# print(num_lisat)

for i in range(a):
    if num_list[i] != 0:
        for j in range(num_list[i]): # 중복된 개수의 숫자 (즉, 2이상일 수가 있다)
            print(i)