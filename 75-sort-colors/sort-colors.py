class Solution(object):
    def sortColors(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=dict(sorted(d.items()))
        index=0
        for j in s:
            for i in range(s[j]):
                nums[index]=j
                index+=1
    


        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        