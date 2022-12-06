class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-count, char) for char, count in Counter(s).items()]
        heapify(h)
        
        ans = []
        while len(h) > 1:
            ch1_count, ch1 = heappop(h)
            ch2_count, ch2 = heappop(h)
            
            ans.append(ch1)
            ans.append(ch2)
            
            if ch1_count < -1:
                heappush(h, (ch1_count + 1, ch1))
            if ch2_count < -1:
                heappush(h, (ch2_count + 1, ch2))
        
        if h:
            count, ch = heappop(h)
            if count < -1:
                return ""
            ans.append(ch)
        return "".join(ans)
        
            