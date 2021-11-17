class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        q = deque(s)
        
        ops = sum(amount if direction else -amount for direction, amount in shift)
        if ops > 0:
            for _ in range(ops):
                q.appendleft(q.pop())
        else:
            for _ in range(-ops):
                q.append(q.popleft())
                
        return "".join(q)