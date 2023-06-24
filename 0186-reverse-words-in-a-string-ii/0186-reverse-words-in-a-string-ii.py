class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1
                
        end = len(s) - 1
        reverse(0, end)
        
        l = 0
        for i in range(end + 1):
            if s[i] == " " or i == end:
                r = (i - 1) if i < end else i
                reverse(l, r)
                l = i + 1