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
            if nums[i]==c:
                if i==0 or nums[i-1]!=nums[i]:
                    c+=1
            elif nums[i]>c:
                return c
            
        return (c)
        

    
        """
        :type nums: List[int]
        :rtype: int
        """
        