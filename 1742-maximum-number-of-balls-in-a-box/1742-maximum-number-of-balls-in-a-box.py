class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballCounts = {}
        maxBallCount = 0
        for ball in range(lowLimit, highLimit + 1):
            box = 0
            while ball > 0:
                ball, digit = divmod(ball, 10)
                box += digit
            ballCounts[box] = ballCounts.get(box, 0) + 1
            maxBallCount = max(maxBallCount, ballCounts[box])
        return maxBallCount
        