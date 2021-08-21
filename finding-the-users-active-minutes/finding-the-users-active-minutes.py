class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam_map = {}
        for user, minute in logs:
            uam_map.setdefault(user, set()).add(minute)
        
        result = [0] * k
        for minutes in uam_map.values():
            result[len(minutes) - 1] += 1
        
        return result