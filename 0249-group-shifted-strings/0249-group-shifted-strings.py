class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        shiftMap = defaultdict(list)
        for s in strings:
            shift = []
            prev = s[0]
            for i in range(1, len(s)):
                curr = s[i]
                shift.append((ord(curr) - ord(prev)) % 26)
                prev = curr
            shiftMap[tuple(shift)].append(s)
        return list(shiftMap.values())