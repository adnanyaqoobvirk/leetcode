class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def calcPoints(points: int) -> int:
            if T < lower:
                points -= 1
            elif T > upper:
                points += 1
            return points
        
        T = 0
        for i in range(k):
            T += calories[i]

        points = calcPoints(0)
        
        for r in range(k, len(calories)):
            T += calories[r]
            T -= calories[r - k]

            points = calcPoints(points)
        return points
