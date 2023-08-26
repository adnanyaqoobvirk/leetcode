class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        
        res, pend = 0, -inf
        for start, end in pairs:
            if start > pend:
                res += 1
                pend = end
        
        return res