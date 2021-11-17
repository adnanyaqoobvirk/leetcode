class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        q = deque(s)
        for direction, amount in shift:
            if direction:
                for _ in range(amount):
                    q.appendleft(q.pop())
            else:
                for _ in range(amount):
                    q.append(q.popleft())
        return "".join(q)