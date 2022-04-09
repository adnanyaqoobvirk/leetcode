class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts, freq_map, max_freq = Counter(nums), defaultdict(list), 0
        for num, count in counts.items():
            freq_map[count].append(num)
            max_freq = max(max_freq, count)
        
        ans = []
        for count in reversed(range(1, max_freq + 1)):
            for num in freq_map[count]:
                ans.append(num)
                if len(ans) == k:
                    break
            else:
                continue
            break
        return ans