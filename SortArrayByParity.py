class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        y = []
        z = []
        mask = 1
        for i in range(len(A)):
            if A[i] & mask == 0:
                y.append(A[i])
            else:
                z.append(A[i])
        a = y + z
        return a

