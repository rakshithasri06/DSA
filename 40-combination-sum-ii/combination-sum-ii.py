class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return

            for j in range(i, len(candidates)):
                # Skip duplicates at the same recursion level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Since array is sorted, no later number can work
                if total + candidates[j] > target:
                    break

                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

        dfs(0, [], 0)
        return res