class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_d = 0
        for i, s in enumerate(seats):
            if s == 0:
                max_d = i + 1
            else:
                break
        
        prev_full = i
        for j in range(i + 1, len(seats)):
            if seats[j] == 1:
                max_d = max(max_d, (j - prev_full) // 2)
                prev_full = j
        
        max_d = max(max_d, len(seats) - 1 - prev_full)
        return max_d