nums = [1,2,3,1]
for idx,num in enumerate(nums):
    pivot = num;
    for next_num in nums[idx::]:
        if next_num == pivot:
            print('True')
            break;
            # return true;
print('false')
# return False

# 이중 for문을 통해 굉장히 많은 시간이 걸렸는데,

# #이렇게 쓸경우 O(N)을 통해 정답으로 판정되었다.
#     """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         # return len(set(nums)) != len(nums)
#         s = set();
#         for num in nums:
#             if num in s:
#                 return True;
#             s.add(num)
#         return False
            
#         # return False