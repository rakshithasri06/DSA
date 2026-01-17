class Solution(object):
    def generateParenthesis(self, n):
        stack=[]
        res=[]

        def backtracking(openn,closen):
            
            if openn==closen==n:
                res.append("".join(stack))
                return res
            if openn<n:
                stack.append("(")
                backtracking(openn+1,closen)
                stack.pop()
            if openn>closen:
                stack.append(")")
                backtracking(openn,closen+1)
                stack.pop()
        backtracking(0,0)
        return(res)
        """
        :type n: int
        :rtype: List[str]
        """
        