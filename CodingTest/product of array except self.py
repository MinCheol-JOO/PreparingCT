# nums = [0,0]

nums = [-1,1,0,-3,3]
# # nums = [2,3,0,0]
# p = 0
# new_nums = float('inf')
# idx_0 = -1
# new_numlist = []

# for idx,num in enumerate(nums) :
#     if num == 0 and idx_0 !=-1:
#         print([0 for i in range(len(nums))])
#     if idx == 0 and num != 0:
#         p +=1
#     if num == 0 :
#         idx_0 = idx 
#         continue;
#     p = p*num;
# # new_nums.append(p)
# print(p)

# for i in nums:
#     if idx_0 !=-1:
#         if i ==0 and min(nums): # nums값에서 만약에 0이 두개이상일 경우
#             new_numlist.append(p);
#         else:
#             new_numlist.append(0);
#     else:
#         a = p/i
#         new_numlist.append(int(a))
# print(new_numlist)

nums = [-1,1,0,-133,3]
left = 1;
right =1
ans = [1 for _ in nums]
for i in range(len(nums)):
    ans[i] *= left # ans[0] = 1   ans[1] = 1*-1 ans[2]= 1
    ans[~i] *= right # ans[-1] = 1 ans[-2] = 1*3
    left *= nums[i] # left = -1 left = -1
    right *= nums[~i] # right = 3 right = -9
    print(ans)

    # 생각해보면, 첫번째 원소를 한번 계산해놓고 이를 ans에 넣어놓으면, 마지막에 right에 들어오는 원소와 곱해버리면 최종 값이랑 같다!
    # 이걸 바탕으로 코딩한 것이네.
    #  



