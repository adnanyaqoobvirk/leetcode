class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h = [(-ord(char), -count) for char, count in Counter(s).items()]
        heapify(h)
        
        res = []
        prev_count, prev_char = 0, inf
        while h:
            ochar, count = heappop(h)
            
            if prev_count < 0 and prev_char < ochar:
                res.append(chr(-ochar))
                count += 1
            else:
                if -count > repeatLimit:
                    res.append(repeatLimit * chr(-ochar))
                    count += repeatLimit
                else:
                    res.append(chr(-ochar) * -count)
                    count = 0
            
            if prev_count < 0:
                heappush(h, (prev_char, prev_count))
            
            prev_char, prev_count = ochar, count
        
        return "".join(res)