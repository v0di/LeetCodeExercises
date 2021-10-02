class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I':1, 'V':5, 'X':10, 'L':50,
            'C':100, 'D':500, 'M':1000
        }
        integer = 0
        for index in range(len(s)):
            try:
                if (n := nums[s[index]]) < nums[s[index+1]]:
                    integer -= n
                else:
                    integer += n
            except IndexError:
                integer += n
        return integer
