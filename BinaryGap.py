class Solution:
    def binaryGap(self, N: int) -> int:
        index = 31
        previous = None
        answer = 0
        while N:
            if N & 1 == 1:
                if previous != None:
                    answer = max(answer, 32 - index - previous)
                previous = 32 - index
            N >>= 1
            index -= 1
        return answer

