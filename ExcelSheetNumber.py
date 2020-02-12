class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for index,letter in enumerate(s):
            result += (ord(letter) - 64) * (26 **(len(s) - index - 1))
        return result