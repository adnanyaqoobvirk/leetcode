class Solution:
    def balancedStringSplit(self, s: str) -> int:
        char_count = 0
        balance_count = 0
        for c in s:
            if c == 'R':
                char_count += 1
            else:
                char_count -= 1
            
            if char_count == 0:
                balance_count += 1
        return balance_count