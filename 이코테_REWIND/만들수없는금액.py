n = int(input())
# for _ in range(n):
list_num = list(map(int,input().split()))

list_num.sort()
tmp = []
for i in range(1,sum(list_num)):
    tmp.append(i)

for i in range(len(list_num)+1):
    sum_first_all = sum(list_num[:i])
    sum_last_all = sum(list_num[i:])
    if sum_first_all in tmp:
        tmp.remove(sum_first_all)
    if sum_last_all in tmp:
        tmp.remove(sum_last_all)
tmp.sort()
print(tmp[0])
