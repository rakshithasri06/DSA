class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2


            if nums[middle] == target:
                return True
            elif nums[l]==nums[middle]==nums[r]:
                l+=1
                r-=1
            elif nums[l] <= nums[middle]:#left half is sorted
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1

            # Right half is sorted
            else:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1

        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        