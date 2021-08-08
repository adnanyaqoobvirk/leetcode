class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max_candies = max(candies)
        return [
            True if c + extraCandies >= current_max_candies else False 
            for c in candies
        ]