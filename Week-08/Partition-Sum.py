# 416. Partition Equal Subset Sum

class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [0] * (target + 1)
        dp[0] = 1 

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = 1

        if dp[target]:
            return True
        else:
            return False
