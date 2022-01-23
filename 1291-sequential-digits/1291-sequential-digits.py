class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def helper(start: int, num: int) -> None:
            if low <= num <= high:
                ans.append(num)
            if num < high and start <= 9:
                helper(start + 1, num * 10 + start)
        ans = []
        for d in range(1, 10):
            helper(d, 0)
        return sorted(ans)
                    