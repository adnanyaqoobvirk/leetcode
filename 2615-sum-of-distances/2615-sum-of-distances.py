class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)

        ans = [0] * len(nums)
        for num, indices in idx_map.items():
            psums = [0]
            curr_sum = 0
            for i in indices:
                curr_sum += i
                psums.append(curr_sum)

            for i, idx in enumerate(indices):
                suffix = psums[-1] - psums[i + 1]
                prefix = psums[i]
                ans[idx] = suffix - (len(indices) - 2 * i - 1) * idx - prefix
        
        return ans