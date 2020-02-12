class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(s.maketrans("","",string.punctuation)).replace(" ","").lower()
        if s[::-1] == s:
            return True
        return False