class Solution(object):
    def moveZeroes(self, nums):
        left=right=0
        if len(nums)==0:
            return nums
        while right<len(nums):
            if nums[left]==nums[right]:
                right+=1
            elif nums[left]==0 and (left<right):
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
                left+=1
            else:
                left+=1
        

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        