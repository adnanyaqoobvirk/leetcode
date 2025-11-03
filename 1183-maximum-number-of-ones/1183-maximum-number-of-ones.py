class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        freq = defaultdict(int)
        for i in range(width):
            for j in range(height):
                freq[(i % sideLength, j % sideLength)] += 1
        return sum(sorted(freq.values(), reverse=True)[:maxOnes])