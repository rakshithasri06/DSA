class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        for ch in set(s):
            if s.count(ch) < k:
                parts = s.split(ch)

                ans = 0

                for part in parts:
                    ans = max(ans, self.longestSubstring(part, k))

                return ans

        return len(s)