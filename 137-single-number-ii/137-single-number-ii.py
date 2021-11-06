class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = [0] * 32
        for num in nums:
            for i in range(32):
                if (1 << i) & num:
                    seen[i] += 1
        ans = 0
        for i, count in enumerate(seen):
            if count != 0 and count % 3 != 0:
                ans += (1 << i)
        return ans if seen[31] % 3 == 0 else ans - (1 << 32) 