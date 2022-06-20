class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie, enc_len = {}, 0
        for word in words:
            t = trie
            for c in reversed(word):
                if '$' in t:
                    enc_len -= t['$']
                    del t['$']
                if c not in t:
                    t[c] = {}
                t = t[c]
            if not t:
                t['$'] = len(word) + 1
                enc_len += t['$']
        return enc_len