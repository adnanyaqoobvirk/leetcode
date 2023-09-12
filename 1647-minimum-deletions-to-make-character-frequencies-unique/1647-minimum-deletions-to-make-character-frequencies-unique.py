class Solution:
    def minDeletions(self, s: str) -> int:
        h = [-count for _, count in Counter(s).items()]
        heapify(h)
        
        res = 0
        while h:
            count = heappop(h)
            
            while h and h[0] == count:
                ncount = heappop(h) + 1
                if ncount != 0:
                    heappush(h, ncount)
                res += 1
                
        return res