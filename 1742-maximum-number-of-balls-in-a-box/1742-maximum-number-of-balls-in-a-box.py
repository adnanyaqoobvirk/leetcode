class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballCounts = [0] * 46
        for ball in range(lowLimit, highLimit + 1):
            box = 0
            while ball > 0:
                ball, digit = divmod(ball, 10)
                box += digit
            ballCounts[box] += 1
        return max(ballCounts)