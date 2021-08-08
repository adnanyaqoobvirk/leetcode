class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gauge = max(candies) - extraCandies
        return [
            True if c >= gauge else False 
            for c in candies
        ]