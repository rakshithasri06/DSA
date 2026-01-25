class Solution(object):
    def minimumDifference(self, nums, k):
        left=0
        min_diff=float("inf")

        for right in range(k,len(nums)+1):
            nums.sort()
            window=nums[left:right]
            diff=nums[right-1]-nums[left]
            min_diff=min(min_diff,diff)

            left+=1
        return(min_diff)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        