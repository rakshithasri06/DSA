class Solution(object):
    def maxSubArray(self, nums):

        maxi = float("-inf")
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]

            if sums > maxi:
                maxi = sums

            if sums < 0:
                sums = 0

        return(maxi)
        """
        :type nums: List[int]
        :rtype: int
        """
        