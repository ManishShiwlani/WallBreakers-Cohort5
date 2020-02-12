class Solution:
    def findComplement(self, num: int) -> int:
        x = len(bin(num)) - 2
        return (num ^ ((2 ** x) - 1))
