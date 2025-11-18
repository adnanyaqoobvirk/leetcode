class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        prev = 0
        ans = True
        for curr in bits:
            ans = prev == 0 and curr == 0
            prev = 0 if prev == 1 and curr == 1 else curr
        return ans