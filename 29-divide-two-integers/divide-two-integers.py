class Solution(object):
    def divide(self, dividend, divisor):

        divid = abs(dividend)
        divis = abs(divisor)

        result = 0

        while divid >= divis:

            temp = divis
            count = 1

            while divid >= temp + temp:
                temp += temp
                count += count

            divid -= temp
            result += count

        if (dividend < 0) != (divisor < 0):
            result = -result

        if result > 2**31 - 1:
            result = 2**31 - 1

        return result