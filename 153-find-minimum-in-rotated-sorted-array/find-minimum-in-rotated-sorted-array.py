class Solution(object):
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        small=nums[0]
        while l<=r:
            mid=(l+r)//2
            small=min(small,nums[mid])
            if nums[r]<nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return small
        """
        :type nums: List[int]
        :rtype: int
        """
        