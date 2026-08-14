class Solution(object):
    def searchMatrix(self, matrix, target):
        i=0
        j=len(matrix[0])-1
        while i<len(matrix) and j>=0: 
            if matrix[i][j]==target:
                return True
                break
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False
        

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        