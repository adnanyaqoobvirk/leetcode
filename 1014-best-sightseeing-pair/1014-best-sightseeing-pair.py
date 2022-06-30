class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        curr_picked, curr_unpicked = values[n - 1] - n + 1, -inf
        for pos in reversed(range(n - 1)):
            curr_picked, curr_unpicked = max(
                values[pos] - pos,
                curr_picked
            ), max(
                curr_unpicked,
                values[pos] + pos + curr_picked
            )
        return curr_unpicked