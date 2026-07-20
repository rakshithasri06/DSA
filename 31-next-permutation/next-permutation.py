class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        index = -1

        # Find the first decreasing element from the end
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If such an element exists, swap it
        if index != -1:
            for i in range(n - 1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break

        # Reverse the suffix
        nums[index + 1:] = nums[index + 1:][::-1]

        return (nums)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        