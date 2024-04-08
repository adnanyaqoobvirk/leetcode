class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        p = 0
        n = len(sandwiches)
        r = 0
        while p < n and r < len(q):
            if q[0] == sandwiches[p]:
                p += 1
                r = 0
                q.popleft()
            else:
                q.append(q.popleft())
                r += 1
        return len(q)