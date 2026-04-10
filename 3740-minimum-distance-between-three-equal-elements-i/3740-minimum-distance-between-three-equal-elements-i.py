class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[i] != nums[k]:
                        continue

                    ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))
        return -1 if ans == inf else ans