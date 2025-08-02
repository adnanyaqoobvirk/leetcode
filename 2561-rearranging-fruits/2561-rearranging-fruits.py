class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1Counts = Counter(basket1)
        b2Counts = Counter(basket2)
        sortedUniques = sorted(b1Counts.keys() | b2Counts.keys())
        minv = sortedUniques[0]
        ans = 0
        l, r = 0, len(sortedUniques) - 1
        while l <= r:
            ul, ur = sortedUniques[l], sortedUniques[r]
            if b1Counts[ur] == b2Counts[ur]:
                r -= 1
                continue
            if b1Counts[ul] == b2Counts[ul]:
                l += 1
                continue
            
            if abs(b1Counts[ur] - b2Counts[ur]) & 1:
                return -1
            if abs(b1Counts[ul] - b2Counts[ul]) & 1:
                return -1
            
            if 2 * minv >= ul:
                ans += ul
                if b1Counts[ul] > b2Counts[ul]:
                    b2Counts[ul] += 1
                    b1Counts[ul] -= 1
                else:
                    b2Counts[ul] -= 1
                    b1Counts[ul] += 1
            else:
                ans += minv

            if b1Counts[ur] > b2Counts[ur]:
                b2Counts[ur] += 1
                b1Counts[ur] -= 1
            else:
                b2Counts[ur] -= 1
                b1Counts[ur] += 1
        return ans