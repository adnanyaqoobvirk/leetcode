class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        word_len_map = defaultdict(list)
        for i, word in enumerate(words):
            word_len_map[len(word)].append(i)
        
        dp = [1] * (n + 1)
        ans = 1
        for l in reversed(range(1, 16)):
            for pos in word_len_map[l]:
                for i in word_len_map[len(words[pos]) + 1]:
                    prev = -1
                    for c in words[pos]:
                        j = words[i].find(c, prev + 1)
                        if j <= prev:
                            break
                        prev = j
                    else:
                        dp[pos] = max(dp[pos], 1 + dp[i])
                ans = max(ans, dp[pos])
        return ans
            