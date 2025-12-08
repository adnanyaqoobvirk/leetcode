class Solution:
    def countTriples(self, n: int) -> int:
        squares = [num**2 for num in range(1, n + 1)]
        square_triples = 0
        for i, target in enumerate(squares):
            left, right = 0, i - 1
            while left < right:
                total = squares[left] + squares[right]
                if total == target:
                    square_triples += 2
                    left += 1
                    right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return square_triples