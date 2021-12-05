class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans, counts = [], Counter(digits)
        for d1 in range(1, 10):
            for d2 in range(10):
                for d3 in range(0, 10, 2):
                    if counts[d1] > 0 and counts[d2] > (d1 == d2) and counts[d3] > (d3 == d1) + (d3 == d2):
                        ans.append(d1 * 100 + d2 * 10 + d3)
        return ans