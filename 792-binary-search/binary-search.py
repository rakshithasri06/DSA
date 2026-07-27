class Solution(object):
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            middle= (l+r)//2
            if nums[middle]==target:
                return (middle)
    
            elif target>nums[middle]:
                l=middle+1
            else:
                r=middle-1 
        return (-1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        