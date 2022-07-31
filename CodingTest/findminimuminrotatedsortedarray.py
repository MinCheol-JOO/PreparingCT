nums = [3,4,5,1,2]
i = 0 
j = len(nums)-1

while i<j:
    m = i+(j-i)//2 # 계속해서 반으로 줄이는 그러한 알고리즘을 사용하라는 얘기였구나
    if nums[m]>nums[j]:
        i=m+1
    else:
        j=m
print(nums[i])
    