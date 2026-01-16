# Optimal solution 

def sortArray(nums):
    n, count0 , count1, count2 = len(nums), 0, 0, 0
    #O(n)
    for i in range(n):
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        else:
            count2 += 1

    #O(n)    
    idx = 0
    for i in range(count0):
        nums[idx] = 0
        idx += 1
    for i in range(count1):
        nums[idx] = 1
        idx += 1
    for i in range(count2):
        nums[idx] = 2
        idx += 1
    return nums

nums = [2,0,2,1,1,0,1,2,0,0]
print(sortArray(nums)) # over all O(2n) :-> O(n) TC SC O(1)

# Most optimaal solution that is Dutch National Falg Algorithm single pass

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

print(dutchsortArray(nums))


        