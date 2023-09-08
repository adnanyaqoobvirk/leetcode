class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-count, char) for char, count in Counter(s).items()]
        heapify(h)
        
        if -h[0][0] > math.ceil(len(s) / 2):
            return ""
        
        res = []
        while h:
            count, char = heappop(h)
            
            if h and res and res[-1] == char:
                count2, char2 = heappop(h)
                
                res.append(char2)
                if count2 + 1 != 0:
                    heappush(h, (count2 + 1, char2))
                heappush(h, (count, char))
            else:
                res.append(char)
                if count + 1 != 0:
                    heappush(h, (count + 1, char))
        return "".join(res)