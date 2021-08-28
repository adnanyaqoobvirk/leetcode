class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        char_pos = {}
        for i, c in enumerate(word):
            char_pos.setdefault(c, []).append(i)
        
        count = 0
        for pat in patterns:
            for pos in char_pos.get(pat[0], []):
                for c in pat:
                    if pos >= len(word) or word[pos] != c:
                        break
                    pos += 1
                else:
                    count += 1
                    break
        return count