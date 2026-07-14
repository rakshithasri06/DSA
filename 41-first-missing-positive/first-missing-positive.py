class Solution(object):
    def firstMissingPositive(self, nums):
        """if len(nums)==1:
            if nums==[1]:
                return (2)
            else:
                return (1)
        nums.append(0)"""
        nums.sort()
        c=1
        d=len(nums)
        for i in range(0,d):
            if nums[i]<=0:
                continue
            elif nums[i]==c:
                if d or nums[i-1]!=nums[i]:
                    c+=1
            
        return (c)
        

    
        """
        :type nums: List[int]
        :rtype: int
        """
        