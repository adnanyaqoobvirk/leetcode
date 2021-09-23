class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for count in Counter(arr).values():
            if count in seen:
                return False
            seen.add(count)
        return True