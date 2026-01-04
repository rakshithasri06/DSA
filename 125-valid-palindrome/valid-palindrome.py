class Solution(object):
    def isPalindrome(self, s):
        d=''
        for i in s:
            if i.isalnum():
                d+=i.lower()
        return d==d[::-1]

        """
        :type s: str
        :rtype: bool
        """
        