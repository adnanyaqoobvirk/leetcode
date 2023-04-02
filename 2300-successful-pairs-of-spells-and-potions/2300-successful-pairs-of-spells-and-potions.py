class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        m = len(potions)
        
        pairs = []
        for spell in spells:
            min_multiple = ceil(success / spell) - 1
            
            lo, hi = 0, m
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if potions[mid] > min_multiple:
                    hi = mid
                else:
                    lo = mid + 1
                    
            pairs.append(m - lo)
        return pairs