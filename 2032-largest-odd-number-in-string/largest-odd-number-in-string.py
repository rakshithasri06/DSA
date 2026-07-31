class Solution(object):
    def largestOddNumber(self, num):
        while num:
            if (int(num[-1]))%2 != 0:
                return num
            else:
                num = num[0:-1]
        return ("")
        """
        :type num: str
        :rtype: str
        """
        