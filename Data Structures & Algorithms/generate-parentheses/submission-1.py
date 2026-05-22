class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def bt(open,close):
            if open==close==n:
                res.append("".join(stack))
                return
            if open<n:
                stack.append("(")
                bt(open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                bt(open,close+1)
                stack.pop()
        bt(0,0)
        return res