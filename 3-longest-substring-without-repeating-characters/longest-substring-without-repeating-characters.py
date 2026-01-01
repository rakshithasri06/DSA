class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        max_len=0

        for right in range(0,len(s)):
            while s[right] in s[left:right]:
                left+=1
            max_len=max(max_len,right-left+1)

        return(max_len)
        # start = 0
        # seen = set()
        # longest = 0

        # for end in range(len(s)):
        #     while s[end] in seen:
        #         seen.remove(s[start])
        #         start += 1

        #     seen.add(s[end])
        #     longest = max(longest, end - start + 1)

        # return longest
