# amount = int(input())

# list_number = []
# a = int(input())
# arr = list(map(int,input().split()))

# # 값 저장

# list_number_1 =list(set(list_number))
# # set을 통해 중복값들 삭제

# list_cal = [] # 밑에 있는 아이들의 개수
# # 만약에 list_number_1에 계산한 값이 없다면
# # i(idx 1씩 증가하는)를 기준으로 잡고 여기보다 작은 아이들을 센다

# list_cal_dict = dict()
# # for i in range(amount):
# #     list_cal_dict[list_number[i]]=[] #리스트 넘버가 idx가 된다


# for i in range(amount):
#     cnt = 0
#     if list_number[i] in list_cal_dict:
#         print(list_cal_dict[list_number[i]])
#     else:
#         for j in range(len(list_number_1)):
#             if list_number[i]>list_number_1[j]:
#                 cnt+=1
#         list_cal_dict[list_number[i]]=cnt
#         # list_cal_dict[list_number_1[i]]=cnt;
#         print(cnt)


# # 백준에서 컴파일에러 나옴


# 이것이 답
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

# 제일작은거 : 몇개인지 숫자
dic = {arr2[i] : i for i in range(len(arr2))} # i가 몇번째인지를 알려주는 dictionary
# print(dic)
for i in arr:
    print(dic[i], end = ' ')