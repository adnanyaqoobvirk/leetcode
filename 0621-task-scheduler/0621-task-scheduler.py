class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [-count for count in Counter(tasks).values()]
        heapify(h)
        
        res = 0
        while h:
            count = heappop(h)
            counts = [count + 1] if count < -1 else []
            res += 1
            
            i = n
            while h and i > 0:
                count = heappop(h)
                if count < -1:
                    counts.append(count + 1)
                res += 1
                i -= 1
            
            if counts:
                res += i
            
            for count in counts:
                heappush(h, count)
        return res                
                
                    
                    