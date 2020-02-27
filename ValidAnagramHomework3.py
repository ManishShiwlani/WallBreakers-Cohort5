class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        elif len(s) != len(t):
            return False
        elif len(s) and len(t) == 1 and s != t:
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False