class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, lo, hi = 0, 0, len(people) - 1
        while lo <= hi:
            if people[hi] + people[lo] > limit:
                boats += 1
                hi -= 1
            else:
                boats += 1
                hi -= 1
                lo += 1
        return boats