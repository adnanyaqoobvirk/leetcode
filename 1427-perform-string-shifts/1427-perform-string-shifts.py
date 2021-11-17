class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        q = deque(s)
        
        shifts = 0
        for direction, amount in shift:
            if direction:
                shifts += amount
            else:
                shifts -= amount
                
        if shifts > 0:
            for _ in range(shifts):
                q.appendleft(q.pop())
        else:
            for _ in range(-shifts):
                q.append(q.popleft())
                
        return "".join(q)