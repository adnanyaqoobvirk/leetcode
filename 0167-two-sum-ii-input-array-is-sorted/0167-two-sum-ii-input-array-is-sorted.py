class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2

            curr = numbers[lo] + numbers[hi]

            if curr == target:
                return [lo + 1, hi + 1]
            elif curr > target:
                if numbers[lo] + numbers[mid] >= target:
                    hi = mid
                else:
                    hi -= 1
            else:
                if numbers[hi] + numbers[mid] <= target:
                    lo = mid
                else:
                    lo += 1