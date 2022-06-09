class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr = numbers[lo] + numbers[hi]
            if curr > target:
                if numbers[lo] + numbers[mid] < target:
                    hi = hi - 1
                else:
                    hi = mid
            elif curr < target:
                if numbers[hi] + numbers[mid] > target:
                    lo = lo + 1
                else:
                    lo = mid
            else:
                return [lo + 1, hi + 1]