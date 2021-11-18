class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(start: int, end: int) -> None:
            for i in range((end - start) // 2 + 1):
                s[start + i], s[end - i] = s[end - i], s[start + i]
        
        reverse(0, len(s) - 1)
        w_start = w_end = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(w_start, i - 1)
                w_start = w_end = i + 1
        reverse(w_start, i)