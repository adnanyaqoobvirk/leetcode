class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = runSum = 0
        for num in reversed(satisfaction):
            runSum += num
            if runSum <= 0:
                break
            ans += runSum
        return ans