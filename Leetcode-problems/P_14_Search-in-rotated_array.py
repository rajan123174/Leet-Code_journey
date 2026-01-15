def rotatedSortedArray(nums,target):
    start = 0 
    end = len(nums)

    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:# Left sorted array
            if nums[start] <= target and target <= nums[mid]:# left half
                end = mid-1
            else:
                start = mid+1 # right half

        else: # right sorted array
            if nums[mid] <= target and target <= nums[end]: # left half of right
                start = mid+1 
            else:
                end = mid-1 # right
    return -1
    
nums = [4,5,6,7,0,1,2]
target = 0

print(rotatedSortedArray(nums,target))




        