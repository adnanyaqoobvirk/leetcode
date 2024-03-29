class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr_penalty = min_penalty = min_hour = 0
        
        for i, c in enumerate(customers):
            curr_penalty += -1 if c == 'Y' else 1
            
            if curr_penalty < min_penalty:
                min_hour = i + 1
                min_penalty = curr_penalty
        
        return min_hour