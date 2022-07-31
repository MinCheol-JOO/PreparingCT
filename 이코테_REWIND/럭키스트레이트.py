# 럭키스트레이트
input_num = list(map(int,input()))
# print(input_num)
first = input_num[:len(input_num)//2]
last = input_num[len(input_num)//2:]
if sum(first) == sum(last):
    print('LUCKY')
else:
    print('READY')