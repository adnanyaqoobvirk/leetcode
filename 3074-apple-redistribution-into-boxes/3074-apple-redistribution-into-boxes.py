class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apple_count = sum(apple)
        for i in range(len(capacity)):
            apple_count -= capacity[i]
            if apple_count <= 0:
                return i + 1
        return len(capacity)
            