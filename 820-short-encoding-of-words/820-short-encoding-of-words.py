class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        
        trie, enc_len = {}, 0
        for word in words:
            t = trie
            for c in reversed(word):
                if c not in t:
                    t[c] = {}
                t = t[c]
            if '$' not in t:
                t['$'] = len(word) + 1
                if len(t) == 1:
                    enc_len += t['$']
        return enc_len