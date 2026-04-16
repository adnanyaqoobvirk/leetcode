class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)
        
        ans = []
        for j in queries:
            indices = idx_map[nums[j]]
            k = len(indices)
            if k <= 1:
                ans.append(-1)
                continue
            
            lo, hi = 0, k - 1
            while lo <= hi:
                mid = (lo + hi) >> 1

                if indices[mid] == j:
                    nxt_dst = abs(j - indices[(mid + 1) % k])
                    pre_dst = abs(j - indices[(mid - 1) % k])
                    min_nxt_dst = min(n - nxt_dst, nxt_dst)
                    min_pre_dst = min(n - pre_dst, pre_dst)
                    if min_nxt_dst < min_pre_dst:
                        ans.append(min_nxt_dst)
                    else:
                        ans.append(min_pre_dst)
                    break
                elif indices[mid] < j:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return ans