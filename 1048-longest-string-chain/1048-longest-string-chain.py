class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def helper(pos: int) -> int:
            max_chain = 1
            for i in word_len_map[len(words[pos]) + 1]:
                prev = -1
                for c in words[pos]:
                    j = words[i].find(c, prev + 1)
                    if j <= prev:
                        break
                    prev = j
                else:
                    max_chain = max(max_chain, 1 + helper(i))
            return max_chain
        
        word_len_map = defaultdict(list)
        for i, word in enumerate(words):
            word_len_map[len(word)].append(i)
        
        return max(helper(k) for k in range(len(words)))