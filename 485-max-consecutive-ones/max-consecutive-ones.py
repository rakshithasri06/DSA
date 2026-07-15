
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=d=0
        l=len(nums)
        for i in range(l):
                
            if nums[i] == 1:
                c=c+1
                d=max(d,c)
            else:
                c=0
        return (d)
        """
        :type nums: List[int]
        :rtype: int
        """
        