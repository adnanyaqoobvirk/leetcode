class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        ycounts = [0] * (n + 1)
        for i in reversed(range(n)):
            ycounts[i] = ycounts[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        hour = min_penalty = n
        penalty = 0
        for i in range(n + 1):
            if penalty + ycounts[i] < min_penalty:
                hour = i
                min_penalty = penalty + ycounts[i]
            if i < n:
                penalty += (1 if customers[i] == 'N' else 0)
            
        return hour