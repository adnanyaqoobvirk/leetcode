from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mapping = SortedDict()
        for i in range(k):
            if nums[i] not in mapping:
                mapping[nums[i]] = set()
            mapping[nums[i]].add(i)
        
        ans = [mapping.keys()[-1]]
        for i in range(k, len(nums)):
            v = nums[i - k]
            mapping[v].remove(i - k)
            if not mapping[v]:
                del mapping[v]
            
            if nums[i] not in mapping:
                mapping[nums[i]] = set()
            mapping[nums[i]].add(i)
            
            ans.append(mapping.keys()[-1])
        return ans