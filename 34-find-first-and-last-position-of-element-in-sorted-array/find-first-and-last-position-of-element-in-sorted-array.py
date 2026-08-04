class Solution(object):
    def searchRange(self, nums, target):
        def lowerbound(nums,target):
            l=0
            ans=len(nums)
            r=ans-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>= target:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            return ans 
        def upperbound(nums,target):
            l=0
            ans=len(nums)
            r=ans-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]> target:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            return ans
        first=lowerbound(nums,target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        last=upperbound(nums,target)-1

        return [first,last]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        