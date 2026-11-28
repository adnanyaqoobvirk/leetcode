class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        odd_seen = False
        for c, count in counts.items():
            if count & 1:
                if odd_seen:
                    return False
                odd_seen = True
        return True