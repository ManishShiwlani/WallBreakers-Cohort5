class Solution:
    def reverseWords(self, s: str) -> str:
        letter = str(s[::-1])
        word_list = letter.split()
        word_list.reverse()
        t = " "
        t = t.join(word_list)
        x = ""
        if s == x:
            return (x)
        for word in s:
            return (t)
