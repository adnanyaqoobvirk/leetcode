class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        count = total = 0
        for num in range(1, n + 1):
            if num not in b:
                total += num
                if total > maxSum:
                    return count
                count += 1
        return count