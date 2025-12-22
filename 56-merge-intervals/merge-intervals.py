class Solution(object):
    def merge(self, interval):
        if not interval:
            return []

        interval.sort()
        result=[interval[0]] #result=[1,3]
        for i in (interval[1:]):
            j=result[-1] #j=[1,3]
            if j[1]>=i[0]: #3>2
                result[-1]=[j[0],max(j[-1],i[-1])]
            else:
                result.append(i)
        return result


        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        