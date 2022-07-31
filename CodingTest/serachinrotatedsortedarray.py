# search in rotated sorted array

# nums = [1]
from xml.dom import minidom


nums = [1,3]
target = 1

# right = len(nums)-1
# binary_search_idx = right//2
# left = 0;

# if not nums:
#     return -1

# low, high = 0, len(nums)-1

# while low<=high:
#     mid = (low + high)/2
#     if target == nums[mid]:
#         return mid
#     if nums[low]<=nums[mid]:
#         if nums[low]<=target<=nums[mid]:
#             high = mid-1
#         else:
#             low = mid+1
#     else:
#         if nums[mid]<=target<=nums[high]:
#             low = mid+1
#         else:
#             high = mid-1

# return -1


# 재귀를 통해서 푸는법
# def binary_search(self,nums,start,end,target):
#     if nums[(start+end)//2] == target:
#         return (start+end)//2
    
#     if start>end:
#         return -1
    
#     if nums[start]<=nums[(start+end)//2]:
#         if nums[start]<=target<nums[(start+end)//2]:
#             return self.binary_search(nums,start,(start+end)//2-1,target)
#         else:
#             return self.binary_serach(nums,(start+end)//2+1,end,target)
    
#     else:
#         if nums[(start+end)//2]<=target<nums[end]:
#             return self.binary_search(nums,(start+end)//2+1,end,target)
#         else:
#             return self.binary_search(nums,start,mid-1,target)



# def search(self,nums,target):
#     return binary_search(self,nums,0,len(nums)-1,target)
