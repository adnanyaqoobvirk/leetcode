class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def count(l: int, r: int) -> int:
            if l == r:
                return 1 if lower <= nums[l] <= upper else 0

            m = l + (r - l) // 2
            left = count(l, m)
            right = count(m + 1, r)
        
            ssums = []
            total = 0
            for i in reversed(range(l, m + 1)):
                total += nums[i]
                ssums.append(total)
            ssums.sort()

            cnt = total = 0
            for i in range(m + 1, r + 1):
                total += nums[i]

                j = bisect_left(ssums, lower - total)
                k = bisect_right(ssums, upper - total)

                cnt += k - j
            return cnt + left + right
        return count(0, len(nums) - 1)