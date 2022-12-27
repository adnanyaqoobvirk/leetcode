class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        full_bags = 0
        for diff in sorted(
            capacity[i] - rocks[i] for i in range(len(capacity))
        ):
            additionalRocks -= diff
            if additionalRocks < 0:
                break
            full_bags += 1
        return full_bags
            