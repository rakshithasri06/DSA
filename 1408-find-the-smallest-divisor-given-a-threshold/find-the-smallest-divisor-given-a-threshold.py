class Solution(object):
    def smallestDivisor(self, nums, threshold):
        l=1
        r=max(nums)

        while l<=r:
            mid=(l+r)//2
            sums=0
            for i in nums:
                sums+=math.ceil(i/float(mid))
            if sums>threshold:
                l=mid+1
            else:
                r=mid-1
        return(l)
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        