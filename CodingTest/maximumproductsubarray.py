nums = [-2,1,-3,4,-1,2,1,-5,4]
tempProMax,tempProMin = [0 for _ in range(len(nums))],[0 for _ in range(len(nums))]
tempProMax[0] = tempProMin[0] = nums[0]

for i in range(1,len(nums)):
    tempProMax[i] = max(tempProMax[i-1]*nums[i], tempProMin[i-1]*nums[i],nums[i])
    tempProMin[i] = min(tempProMax[i-1]*nums[i],tempProMin[i-1]*nums[i],nums[i])

print(max(tempProMax))