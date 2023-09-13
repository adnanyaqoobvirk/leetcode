class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        h = [(-count, char) for char, count in Counter(s).items()]
        heapify(h)
        
        res = []
        while h:
            count, char = heappop(h)
            
            counts = [(count + 1, char)] if count < -1 else []
            res.append(char)
            
            for _ in range(k - 1):
                if not h:
                    if count < -1:
                        return ""
                    break
                    
                ncount, nchar = heappop(h)
                if ncount < -1:
                    counts.append((ncount + 1, nchar))
                res.append(nchar)
            
            for count, char in counts:
                heappush(h, (count, char))
        return "".join(res)