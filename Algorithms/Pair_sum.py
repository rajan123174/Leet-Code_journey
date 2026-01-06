# this is for printing all unique pairs
'''def pairSum(nums,pair):  
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            print(nums[i],nums[j])'''

# This is an Brute force approach time complexity :-> O(n2)
def pairSum(nums,pair,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                pair.append((i,j))
    return pair


nums = [2,7,11,15]
pair = []
target = 9

print(pairSum(nums,pair,target))

'''Here we will think about in other way in the
   QUESTION it is given that the ums array 
   is sorted so we will use that hint to optimize
   or solution
'''


def pairSum_Optimized(nums,target):
    i = 0
    j = len(nums)-1
    while i < j:
        pair_Sum = nums[i]+nums[j]
        if pair_Sum > target:
            j = j-1
        elif pair_Sum < target:
            i = i+1
        else:
           return pair_Sum
        

print(pairSum_Optimized(nums,target))
        
