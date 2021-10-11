class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(1, len(rating) - 1):
            less, more = [0, 0], [0, 0]
            for j in range(len(rating)):
                if rating[j] < rating[i]:
                    less[j > i] += 1
                if rating[j] > rating[i]:
                    more[j > i] += 1
            ans += less[0] * more[1] + less[1] * more[0]
        return ans