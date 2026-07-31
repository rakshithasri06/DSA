class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        pos=len(nums)
        while l<=r:
            middle=(l+r)//2
            if nums[middle]==target:
                pos=middle
                return(pos)
            elif nums[middle] > target :
                pos=middle
                r=middle-1
            else:
                l=middle+1
        return (pos)
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        