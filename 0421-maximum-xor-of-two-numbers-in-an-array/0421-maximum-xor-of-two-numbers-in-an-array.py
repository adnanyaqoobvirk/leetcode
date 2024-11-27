class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        L = len(bin(max(nums))) - 1
        max_xor = 0
        for i in range(len(nums)):
            t1 = t2 = trie
            for j in reversed(range(L + 1)):
                d = (nums[i] >> j) & 1
                if (not d) in t1:
                    t1 = t1[not d]
                elif d in t1:
                    t1 = t1[d]
                if d not in t2:
                    t2[d] = {}
                t2 = t2[d]
            t2["#"] = nums[i]
            if i > 0:
                max_xor = max(max_xor, nums[i] ^ t1["#"])
        return max_xor
            