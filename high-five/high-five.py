class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_scores = {}
        for i, score in items:
            student_scores.setdefault(i, []).append(score)
        
        res = []
        for i in sorted(student_scores.keys()):
            student_scores[i].sort()
            res.append([i, sum(student_scores[i][-1:-6:-1]) // 5])
        return res