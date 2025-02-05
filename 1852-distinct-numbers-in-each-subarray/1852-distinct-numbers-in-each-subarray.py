class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        ans = [len(freq)]
        for i in range(k, len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]
            ans.append(len(freq))
        return ans