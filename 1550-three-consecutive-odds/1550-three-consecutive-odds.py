class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ocount = 0
        for num in arr:
            if num & 1:
                ocount += 1
            else:
                ocount = 0
            if ocount == 3:
                return True
        return False