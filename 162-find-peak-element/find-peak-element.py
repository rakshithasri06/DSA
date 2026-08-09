class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If middle is smaller than next element,
            # peak must be on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Peak is at mid or on the left side
                right = mid

        return left