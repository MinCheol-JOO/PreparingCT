nums = [0,0,0]

# Brute Force
# array = []
# if len(nums)%3 != 0:
#     print(array)


# # # 브루트 포스
# # # 3중 loop를 통해 모든 triplet를 만들어놓고, 각 변수들이 하나의 삼중항 요소에 대해서 추적하도록 한다

# else:
#     for i in range(len(nums)-2) :
#         for j in range(i,len(nums)-1):
#             for k in range(j,len(nums)):
#                 tripet = nums[i]+nums[j]+nums[k]
#                 if i==j or j==k or i==k:
#                     continue;
#                 if tripet == 0:
#                     array.append(sorted([nums[i],nums[j],nums[k]]))
# tpl_array = [tuple(l) for l in array]
# array = set(tpl_array)
# # print(list(array))

# 다른 방법
# if len(nums)<3:
#     return []

res = set()

# 1. split nums into three lists : negative numbers, positive numbers and zeros
n,p,z = [],[],[]
for num in nums:
    if num>0:
        p.append(num)
    elif num<0:
        n.append(num)
    else:
        z.append(num)


# 2. create a separate set for negatives and positves for o(1) look up times
N,P = set(n), set(p)

#3. If there is at least 1 zero in the list, add all cases where -num exist in N and num exists in P
# i.e. (-3,0,3) = 0

if z:
    for num in P : 
        if -1*num in N:
            res.add((-1*num,0,num)) # 이렇게 될 경우에는 반드시 target이 0으로 고정되므로 이렇게 넣음

if len(z)>=3:
    res.add((0,0,0))

#4. for all pairs of negative numbers (-3,1),check to see if their complement (4) exists in the posivie number set
for i in range(len(n)):
    for j in range(i+1,len(p)):
        target = -1*(p[i]+p[j]) # target을 넣어주면 
        if target in N:
            res.add(tuple(sorted(p[i],p[j],target)))


#5 for all pairs of positive numbers (1,1), check to see if their complement (-2) exists in the negative number set
for i in range(len(p)):
    for j in range(i+1,len(n)):
        target = -1*(p[i]+p[j]) # target을 넣어주면 
        if target in P:
            res.add(tuple(sorted(p[i],p[j],target)))
return res

        