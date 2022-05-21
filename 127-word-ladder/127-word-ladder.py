class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        CHARS = 'abcdefghijklmnopqrstuvwxyz'
        
        n = len(beginWord)
        q, wordSet = [beginWord], set(wordList)
        sequence = 1
        while q:
            nq = []
            for s in q:
                if s == endWord:
                    return sequence
                
                for i in range(n):
                    for c in CHARS:
                        ns = f"{s[0:i]}{c}{s[i+1:]}"
                        if ns in wordSet:
                            wordSet.discard(ns)
                            nq.append(ns)
            q = nq
            sequence += 1
        return 0