class Solution:
    def isValid(self, s: str) -> bool:
        close = {'(':')', '[':']', '{':'}'}
        left = close.keys()
        queue = []
        for par in s:
            if par in left:
                queue.append(close[par])
            elif not queue or par != queue.pop(): 
                return False
        return True if not queue else False
