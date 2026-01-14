def singleElement(nums):
    st, end = 0, len(nums)-1
    if len(nums) == 1:# corner cases
        return nums[0]

    while st <= end :
        mid = st+(end-st)//2
        if mid == 0 and nums[0] != nums[1]:#corner cases
            return nums[mid]
        if mid == len(nums)-1 and nums[len(nums)-1] != nums[len(nums)-2]:# corner cases
            return nums[mid]
        if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:# corner cases
            return nums[mid]
        if mid%2 == 0:
            if nums[mid-1] == nums[mid]:
                end = mid-1
            else:
                st = mid+1
        else:
            if nums[mid-1] == nums[mid]:
                st = mid+1
            else:
                end = mid-1
    
#nums = [1,1,2,3,3,4,4,8,8]
nums = [3,3,7,7,19,11,11]
print(singleElement(nums))


