class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for c in asteroids:
            ans.append(c)
            
            while len(ans) >= 2 and ans[-2] > 0 and ans[-1] < 0:
                if -ans[-1] > ans[-2]:
                    a = ans.pop()
                    ans.pop()
                    ans.append(a)
                elif -ans[-1] == ans[-2]:
                    ans.pop()
                    ans.pop()
                else:
                    ans.pop()
        return ans