class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strings:
            mapping[
                "".join(
                    f"{(ord(s[i]) - ord(s[i - 1])) % 26:2}" 
                    for i in range(1, len(s))
                )
            ].append(s)
        return mapping.values()