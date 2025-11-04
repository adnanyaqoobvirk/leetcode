class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            freq = Counter(nums[i:i + k])
            x_top = sorted([(v, k) for k, v in freq.items()], reverse=True)[:x]
            x_sum = sum(k * v for k, v in x_top)
            ans.append(x_sum)
        return ans