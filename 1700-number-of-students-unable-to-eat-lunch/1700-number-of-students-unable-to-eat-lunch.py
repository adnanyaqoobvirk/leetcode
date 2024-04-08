class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = r = 0
        for s in students:
            if s == 0:
                c += 1
            else:
                r += 1
                
        for s in sandwiches:
            if s == 0:
                if c == 0:
                    return r
                c -= 1
            else:
                if r == 0:
                    return c
                r -= 1
        return 0