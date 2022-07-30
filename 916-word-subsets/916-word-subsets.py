class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_char_count = [0] * 26
        for word in words2:
            for c, count in Counter(word).items():
                i = ord(c) - ord('a')
                max_char_count[i] = max(max_char_count[i], count)
        
        ans = []
        for word in words1:
            counts = Counter(word)
            for i in range(26):
                if counts[chr(ord('a') + i)] < max_char_count[i]:
                    break
            else:
                ans.append(word)
        return ans