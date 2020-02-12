class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        # condition for termination
        while (left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            # updating pointers
            left += 1
            right -= 1
        return s
