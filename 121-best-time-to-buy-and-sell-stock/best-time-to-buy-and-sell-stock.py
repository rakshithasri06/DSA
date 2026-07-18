class Solution(object):
    def maxProfit(self, nums):
        min_price=nums[0]
        max_profit=0
        for i in range(len(nums)):
            if nums[i]<min_price:
                min_price=nums[i]
            elif nums[i]-min_price>max_profit:
                max_profit=nums[i]-min_price
        return (max_profit)
        """
        :type prices: List[int]
        :rtype: int
        """
        