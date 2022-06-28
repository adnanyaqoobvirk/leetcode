class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        min_val, max_val, counts = min(nums), max(nums), Counter(nums)
        prev = curr = 0
        for num in reversed(range(min_val, max_val + 2)):
            if num not in counts:
                prev = curr
            else:
                prev, curr = curr, max(
                    num * counts[num] + prev,
                    curr
                )
        return curr
            
            