class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        max_freq = 0
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
        
        ans = 0
        for f in freq.values():
            if f == max_freq:
                ans += f
        return ans