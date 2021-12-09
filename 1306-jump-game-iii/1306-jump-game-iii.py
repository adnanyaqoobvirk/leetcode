class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def helper(pos: int) -> bool:
            if pos >= len(arr) or pos < 0 or pos in done:
                return False
            
            if arr[pos] == 0:
                return True
            
            done.add(pos)
            
            return helper(pos + arr[pos]) or helper(pos - arr[pos])
        done = set()
        return helper(start)