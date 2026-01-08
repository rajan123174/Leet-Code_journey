class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18
        
        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                take = nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1])
                skip1 = dp[i + 1][j]
                skip2 = dp[i][j + 1]
                dp[i][j] = max(take, skip1, skip2)
        
        return dp[0][0]
