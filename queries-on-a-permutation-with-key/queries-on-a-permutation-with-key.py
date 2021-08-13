class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = deque(range(1, m + 1))
        output = []
        for q in queries:
            for i in range(m):
                if p[i] == q:
                    output.append(i)
                    p.remove(q)
                    p.appendleft(q)
                    break
        return output