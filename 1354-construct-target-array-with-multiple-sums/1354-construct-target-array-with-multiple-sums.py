class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        total = 0
        for i in range(len(target)):
            total += target[i]
            target[i] = -target[i]
        
        heapify(target)
        
        while -target[0] > 1:
            largest = -heappop(target)
            remaining = total - largest
            
            if remaining == 1:
                return True
            
            x = largest % remaining
            
            if x == 0 or x == largest:
                return False
            
            heappush(target, -x)
            total = total - largest + x
        return True