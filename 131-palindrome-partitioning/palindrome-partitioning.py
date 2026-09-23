class Solution(object):
    def partition(self,s):
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur[:])
                return

            for j in range(i, len(s)):
                part = s[i:j+1]

                if part == part[::-1]:
                    cur.append(part)
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res
        """
        :type s: str
        :rtype: List[List[str]]
        """
        