class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=d=0
        if len(nums)==1 and nums[0]==1:
            return (1)
            
        for i in range(len(nums)):
                
            if nums[i] == 1:
                c=c+1
                if i==(len(nums)-1):
                    if d==0 or d<c:
                        d=c
            else:
                if d<=c:
                    d=c
                
                c=0
        return (d)
        """
        :type nums: List[int]
        :rtype: int
        """
        