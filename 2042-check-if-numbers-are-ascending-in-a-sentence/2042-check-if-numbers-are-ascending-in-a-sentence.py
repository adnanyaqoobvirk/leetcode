class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        digits = set(string.digits)
        curr = prev = 0
        for c in s: 
            if c in digits:
                curr = 10 * curr + (ord(c) - ord('0'))
            elif c == ' ' and curr:
                if curr <= prev:
                    return False
                prev, curr = curr, 0
        return not curr or curr > prev