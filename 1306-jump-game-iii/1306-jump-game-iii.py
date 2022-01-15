class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, q, seen = len(arr), [start], set()
        while q:
            nq = []
            for i in q:
                if i in seen or i < 0 or i >= n:
                    continue
                if arr[i] == 0:
                    return True
                seen.add(i)
                nq.append(i + arr[i])
                nq.append(i - arr[i])
            q = nq
        return False