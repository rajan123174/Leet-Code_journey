# This is brute force approach 
def productArray(nums,n):
    ans = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        ans.append(prod)
    return ans

nums = [1,2,3,4] 
n = len(nums)
print(productArray(nums,n))

#optimal solution that is Suffix and prefix arrays and answer in product of bothe prefix and sufix

def optimalProd(nums, n):
    prefix = [1] * n
    suffix = [1] * n
    ans = [1] * n

    # Build prefix products
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Build suffix products
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # Build answer
    for i in range(n):
        ans[i] = prefix[i] * suffix[i]

    return ans


print(optimalProd(nums,n))

#the most optimised code space cpmlexity in O(1)
def optimalProd2(nums, n):
    ans = [1] * n

    # Build prefix products
    for i in range(1, n):
        ans[i] = ans[i-1] * nums[i-1]

    # Build suffix products
    suffix = 1
    for i in range(n-2, -1, -1):
        suffix *= nums[i+1]
        ans[i] *= suffix
       

    return ans

print(optimalProd2(nums, n))


         
 

