from heapq import heappush, heappushpop

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_scores = {}
        for i, score in items:
            scores = student_scores.setdefault(i, [])
            
            if len(scores) >= 5:
                heappushpop(scores, score)
            else:
                heappush(scores, score)
                
        return [[i, sum(student_scores[i]) // 5] for i in sorted(student_scores)]