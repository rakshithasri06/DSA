class Solution(object):
    def removeOuterParentheses(self, s):
        j = 0
        d = ""

        for i in s:
            if i == "(":
                if j != 0:
                    d += "("
                j += 1

            else:
                j -= 1
                if j != 0:
                    d += ")"

        return (d)
        """
        :type s: str
        :rtype: str
        """
        