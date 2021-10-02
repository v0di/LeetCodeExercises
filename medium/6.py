# ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = ['' for i in range(numRows)]
        x, it = 0, -1
        for char in s:
            rows[x] += char
            if not x%(numRows - 1): it = -it
            x += it
        return ''.join(rows)
