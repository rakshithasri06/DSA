class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        seen = set()
        longest = 0

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            longest = max(longest, end - start + 1)

        return longest
