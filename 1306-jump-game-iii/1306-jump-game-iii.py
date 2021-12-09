class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q, seen = [start], set()
        while q:
            nq = []
            for i in q:
                if 0 <= i < len(arr) and i not in seen:
                    if arr[i] == 0:
                        return True
                    
                    seen.add(i)
                    nq.append(i + arr[i])
                    nq.append(i - arr[i])
            q = nq
        return False