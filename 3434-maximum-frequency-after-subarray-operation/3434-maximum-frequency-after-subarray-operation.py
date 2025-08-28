class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        kcount = len([1 for num in nums if num == k])
        ans = 0
        for num1 in range(1, 51):
            if num1 == k:
                continue

            t = 0
            for num2 in nums:
                v = 0
                if num2 == num1:
                    v += 1
                elif num2 == k:
                    v -= 1
                t = max(v, t + v)
                ans = max(ans, t + kcount)
        return ans
