class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]

        def dfs(i, cur):
            res.append(cur[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()
        dfs(0,[])
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        