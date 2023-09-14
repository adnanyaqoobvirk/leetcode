class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        h = [(-count, char) for char, count in Counter(s).items()]
        heapify(h)
        
        res, q = [], []
        while h:
            q.append(heappop(h))
            
            if len(q) < k:
                continue
            
            for count, char in q:
                if count < -1:
                    heappush(h, (count + 1, char))
                res.append(char)
            
            q = []
        
        for _, char in q:
            res.append(char)
            
        return "".join(res) if len(res) == len(s) else ""