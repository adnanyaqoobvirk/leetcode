class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_ycount = 0
        for c in customers:
            if c == "Y":
                total_ycount += 1
        
        n = len(customers)
        min_penalty = inf
        curr_ycount = 0
        earliest_hour = 0
        for hour, c in enumerate(chain(customers, "N")):
            penalty = hour - curr_ycount + total_ycount - curr_ycount
            if penalty < min_penalty:
                min_penalty = penalty
                earliest_hour = hour
            if c == "Y":
                curr_ycount += 1
        return earliest_hour