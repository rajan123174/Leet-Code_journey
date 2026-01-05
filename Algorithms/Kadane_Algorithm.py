'''for i in range(n):       # This is for printing all possible subarray
    for j in range(i,n):
        print(arr[i:j+1])
 '''

#This is the Brute force Approach 
def max_Sub_Array_Sum(arr):
    n = len(arr)
    max_Sum = float('-inf')
    for i in range(n):
        for j in range(i,n):
            curr_Sum = sum(arr[i:j+1])
            max_Sum = max(max_Sum,curr_Sum)
    
    return max_Sum


arr = [3,-4,5,4,-1,7,-8]
print(max_Sub_Array_Sum(arr))


# Using Kadane's Algorithm The most Optimal solution 


nums = [3,-4,5,4,-1,7,-8]

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

print(maxSubArray(nums))



