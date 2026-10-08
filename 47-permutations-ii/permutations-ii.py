class Solution(object):
    def permuteUnique(self, nums):
        res = []
        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums) and cur[:] not in res:
                res.append(cur[:])
                return

            for i in range(len(nums)):
                if used[i] == False:

                    # choose
                    cur.append(nums[i])
                    used[i] = True

                    # explore
                    dfs(cur)

                    # undo
                    used[i] = False
                    cur.pop()

        dfs([])
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        