class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [] # dp[i]��ʾ��i��β�����������������
        for i, x in enumerate(nums):
            if i == 0:
                dp.append(x)
            else:
                if dp[-1] < 0:
                    dp.append(x)
                else:
                    dp.append(dp[-1] + x)
                    
        return max(dp)