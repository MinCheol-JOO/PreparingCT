from re import A


# 위에서 아래로
n = int(input())
array =[]
for i in range(n):
    array.append(int(input()))

# print(array)
array = sorted(array,reverse = True)
for _ in array:
    print(_, end = ' ')