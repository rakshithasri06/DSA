class Solution(object):
    def reverseWords(self, s):
        l=list(s.split())
        s=''
        rwords=l[::-1]
        rsent=' '.join(rwords)
        return rsent

        """
        :type s: str
        :rtype: str
        """
        