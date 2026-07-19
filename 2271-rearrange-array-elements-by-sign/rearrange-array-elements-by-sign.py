class Solution(object):
    def rearrangeArray(self, nums):
        '''
        change=None
        for i in range(len(nums)):
            if i%2==0:
                if change is not None and nums[i]<0:
                    nums[change],nums[i]=nums[i],nums[change]
                    change=None
                else:
                    change=i
            else:
                if change is not None and nums[i]>0:
                    nums[change],nums[i]=nums[i],nums[change]
                    change=None
                else:
                    change=i
        return (nums)
        '''

        ans = [0] * len(nums)
        pos = 0
        neg = 1

        for x in nums:
            if x > 0:
                ans[pos] = x
                pos += 2
            else:
                ans[neg] = x
                neg += 2

        return (ans)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        