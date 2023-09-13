class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        left_candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_candies[i] = left_candies[i - 1] + 1
        
        right_candies = [1] * n
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                right_candies[i] = right_candies[i + 1] + 1
        
        return sum(max(left, right) for left, right in zip(left_candies, right_candies))