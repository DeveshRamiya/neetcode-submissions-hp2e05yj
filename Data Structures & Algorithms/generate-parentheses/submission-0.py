class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # at a given time no. of opening > no.of closing 
        #at every iteration we can either add "(" or we can add ")"
        # number of open should be n at the end and number of end should be n
        soln = []
        def dfs(arr,Nopen, Nclose):
            if Nopen == Nclose and Nopen == n:
                soln.append("".join(arr))
                return
            if Nopen < n:
                arr.append("(")
                dfs(arr, Nopen + 1, Nclose)
                arr.pop()
            if Nclose < Nopen:
                arr.append(")")
                dfs(arr, Nopen, Nclose + 1)
                arr.pop()
        dfs([],0,0)
        return soln
                
