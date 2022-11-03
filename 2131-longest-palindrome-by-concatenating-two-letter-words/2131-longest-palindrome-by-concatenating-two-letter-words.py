class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        counts = defaultdict(int)
        for word in words:
            pair = word[::-1]
            if counts[pair]:
                ans += 4
                counts[pair] -= 1
            else:
                counts[word] += 1
        
        for word, count in counts.items():
            if count > 0 and word[0] == word[1]:
                ans += 2
                break
        return ans