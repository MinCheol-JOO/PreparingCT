 

n,x = list(map(int,input().split()))

new_array= list(map(int,input().split()))

def binarySearch(array,start,end,target):
   
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            minner = array[mid] 
            maxxer = array[mid]
            cnt_min =0
            cnt_max = 0
            mid_first = mid
            mid_second = mid
            while minner ==array[mid]:
                cnt_min+=1
                minner = array[mid_first-1]
                mid_first-=1                
            while maxxer == array[mid]:
                cnt_max+=1
                maxxer = array[mid_second+1]
                mid_second +=1
            return cnt_max+cnt_min-1
        elif array[mid] > target:
            end = mid-1

        elif array[mid]< target:
            start = mid+1

    return -1


print(binaryFirstSearch(new_array,0,n-1,x))