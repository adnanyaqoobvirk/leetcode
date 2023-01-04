class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        for task, counts in Counter(tasks).items():
            if counts == 1:
                return -1
            
            d, r = divmod(counts, 3)
            if r == 0:
                rounds += d
            else:
                rounds += d + 1
        return rounds
                