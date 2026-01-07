class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        count = len(t)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            if s[right] in need:
                if need[s[right]] > 0:
                    count -= 1
                need[s[right]] -= 1

            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
