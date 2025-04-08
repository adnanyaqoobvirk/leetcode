class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        duplicates = {}
        for k, v in counts.items():
            if v > 1:
                duplicates[k] = v
        nums = nums[::-1]
        ans = 0
        while duplicates:
            for _ in range(3):
                if nums:
                    num = nums.pop()
                    if num in duplicates:
                        duplicates[num] -= 1
                        if duplicates[num] == 1:
                            del duplicates[num]
            ans += 1
        return ans