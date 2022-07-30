class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        char_count = defaultdict(int)
        for word in words2:
            for c, count in Counter(word).items():
                char_count[c] = max(char_count[c], count)
        
        ans = []
        for word in words1:
            counts = Counter(word)
            for c, count in char_count.items():
                if counts[c] < count:
                    break
            else:
                ans.append(word)
        return ans