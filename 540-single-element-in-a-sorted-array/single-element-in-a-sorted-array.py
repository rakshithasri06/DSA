class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            # Pair is valid, single element is on the right
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                # Single element is on the left (including mid)
                r = mid

        return nums[l]
        """
        :type nums: List[int]
        :rtype: int
        """
        