class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def recurse(t1, t2) -> int:
            if "#" in t1 and "#" in t2:
                if t1 != t2:
                    return t1["#"] ^ t2["#"]
                else:
                    return 0
                
            ans = 0
            if 0 in t1 and 0 in t2:
                ans = max(ans, recurse(t1[0], t2[0]))
            if 1 in t1 and 0 in t2:
                ans = max(ans, recurse(t1[1], t2[0]))
            if 0 in t1 and 1 in t2:
                ans = max(ans, recurse(t1[0], t2[1]))
            if 1 in t1 and 1 in t2:
                ans = max(ans, recurse(t1[1], t2[1]))
            return ans
        
        trie = {}
        for num in nums:
            t = trie
            for i in reversed(range(31)):
                d = num >> i & 1
                if d not in t:
                    t[d] = {}
                t = t[d]
            t["#"] = num
        return recurse(trie, trie)