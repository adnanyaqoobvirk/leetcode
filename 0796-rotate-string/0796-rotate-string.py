class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and s in f"{goal}{goal}"