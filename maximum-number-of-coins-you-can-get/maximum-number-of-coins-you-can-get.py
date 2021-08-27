class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def countingSort(nums: List[int]) -> List[int]:
            counts = Counter(nums)
            result = []
            for num in range(1, 10001):
                count = counts.get(num, None)
                if count:
                    for _ in range(count):
                        result.append(num)
            return result
                    
        n = len(piles)
        sorted_piles = countingSort(piles)
        total = 0
        for i in range(1, n // 3 + 1):
            total += sorted_piles[n - 2 * i]
        return total