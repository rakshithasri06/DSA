class Solution(object):
    def searchMatrix(self, matrix, target):

        l=0 
        r=len(matrix)-1
        while l<=r:
            m1=(l+r)//2
            if matrix[m1][0]==target:
                break
            elif matrix[m1][0]>target:
                r=m1-1
            elif matrix[m1][0]<target:
                if matrix[m1][-1]>=target:
                    break
                l=m1+1
        l,r=0,len(matrix[m1])-1
        while l<=r:
            middle=(l+r)//2
            if matrix[m1][middle]==target:
                return True
        
            elif matrix[m1][middle]>target:
                r=middle-1
            else:
                l=middle+1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        