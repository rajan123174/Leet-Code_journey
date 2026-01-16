# Dutch Flag algorithm implementation using three pointers
def dutchsortArray(nums):
    m , h , l = 0 , len(nums)-1, 0

    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[m], nums[h] = nums[h], nums[m] 
            h -= 1
    return nums

nums = [2,0,2,1,1,0,1,2,0,0]
print(dutchsortArray(nums))