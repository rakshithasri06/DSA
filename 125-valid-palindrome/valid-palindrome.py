class Solution(object):
    def isPalindrome(self, s):
        d=''
        for i in s:
            if i.isalnum():
                d+=i.lower()
        if d[::-1]==d:
            return True
        else:
            return False

        """
        :type s: str
        :rtype: bool
        """
        