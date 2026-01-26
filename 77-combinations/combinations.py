class Solution(object):
    def combine(self, n, k):
        result = []

        def backtracking(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()

        backtracking(1, [])
        return result




        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        