class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        fpositions = []
        for f, l in factory:
            fpositions.extend([f] * l)
            
        n, m = len(robot), len(fpositions)
        curr, prev = [0] * (m + 1), [0] * (m + 1)
        curr[m] = inf
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                curr[j] = min(
                    abs(robot[i] - fpositions[j]) + prev[j + 1],
                    curr[j + 1]
                )
            prev, curr = curr, [0] * (m + 1)
            curr[m] = inf
        return prev[0]