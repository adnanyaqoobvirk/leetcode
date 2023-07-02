class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(i: int, t: int) -> int:
            total = sum(num for num in transfers if num > 0)
            
            if i == m:
                if total != 0:
                    return 0
                else:
                    return t
            
            if m - i < total:
                return 0
            
            transfers[requests[i][0]] -= 1
            transfers[requests[i][1]] += 1
            
            ans = backtrack(i + 1, t + 1)
            
            transfers[requests[i][0]] += 1
            transfers[requests[i][1]] -= 1
            
            return max(ans, backtrack(i + 1, t))
        
        m = len(requests)
        transfers = [0] * n
        return backtrack(0, 0)