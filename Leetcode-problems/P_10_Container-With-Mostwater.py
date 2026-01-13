from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, h * width)
            
            # move the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
# Brute force approach 

def maxWater(n,height):
    ans = 0
    for i in range(len(height)):
        for j in range(i,len(height)):
            width = j-i
            hight = min(height[i],height[j])
            area = width * hight
        ans = max(ans,area)
    return ans

height = [1,8,6,2,5,4,8,3,7]
n = len(height)
print(maxWater(n,height))

# Optimal approach i.e Two pointer approach 

def optimalmaxWater(height,n):
    maxWater = 0
    rp = n-1
    lp = 0

    while lp < rp :
        wd = rp - lp
        ht = min(height[lp],height[rp])
        currWater = wd * ht
        maxWater = max(maxWater,currWater)

        if height[lp] < height[rp]:
            lp +=1
        else:
            rp -= 1
    return maxWater

print(optimalmaxWater(height,n))
        



