class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(arr):
            indices[num].append(i)
        
        n, q, seen, jumps = len(arr) - 1, [0], set(), 0
        while q:
            nq = []
            for i in q:
                if i in seen or i < 0 or i > n:
                    continue
                if i == n:
                    return jumps
                seen.add(i)
                nq.append(i + 1)
                nq.append(i - 1)
                for j in indices[arr[i]]:
                    if j != i:
                        nq.append(j)       
                indices[arr[i]].clear()
            q, jumps = nq, jumps + 1
        return jumps