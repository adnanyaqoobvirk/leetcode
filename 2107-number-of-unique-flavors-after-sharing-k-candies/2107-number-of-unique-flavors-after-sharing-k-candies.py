class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counts = Counter(candies)
        for i in range(k):
            counts[candies[i]] -= 1
            if counts[candies[i]] == 0:
                del counts[candies[i]]

        ans = len(counts)
        if k > 0:
            for i in range(k, len(candies)):
                counts[candies[i - k]] += 1
                counts[candies[i]] -= 1
                if counts[candies[i]] == 0:
                    del counts[candies[i]]
                ans = max(ans, len(counts))
        return ans