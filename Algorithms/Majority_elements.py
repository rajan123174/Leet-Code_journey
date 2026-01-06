'''
Majority Elements: ele > n/2
where n is the number of elements in nums
'''

# Brute force approach 
def majority_Element(nums):
    n = len(nums)

    for value in nums:
        frequency = 0
        for ele in nums:
            if ele == value:
                frequency = frequency + 1
        
        if frequency > n/2:
            return value
        
nums = [2,2,2,1,1,1,2]
print(majority_Element(nums))

# Optimised Approach 
def majorityElement(nums):
    nums.sort()
    freq = 1
    ans = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            freq += 1
        else:
            freq = 1
            ans = nums[i]

            if freq > len(nums) // 2:
                return ans

        return ans  # fallback (LeetCode guarantees majority)
 

print(majorityElement(nums))

# most optimal Approach that is moore's voting Algorithm 
def majority_Element_Optimised(nums):
    freq = 0
    ans = 0
    for i in range(len(nums)):
        if freq == 0:
            ans = nums[i]
        if ans == nums[i]:
            freq += 1
        else:
            freq -= 1
    return ans
print(majority_Element_Optimised(nums)) 