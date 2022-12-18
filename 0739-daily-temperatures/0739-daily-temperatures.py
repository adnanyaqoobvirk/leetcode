class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, hottest = [0] * len(temperatures), 0
        for i in reversed(range(len(temperatures))):
            t = temperatures[i]
            if hottest <= t:
                hottest = t
                ans[i] = 0
            else:
                j = i + 1
                while j < len(temperatures):
                    if temperatures[j] > t:
                        ans[i] = j - i
                        break
                    else:
                        j += ans[j]
        return ans