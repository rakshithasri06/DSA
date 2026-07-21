class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0

        for i in s:
            if (i - 1) not in s:      # Start of a sequence
                count = 1
                x = i

                while (x + 1) in s:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return (longest)
        """
        :type nums: List[int]
        :rtype: int
        """
        