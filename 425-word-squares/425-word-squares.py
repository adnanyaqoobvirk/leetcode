class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def getWords(p: str) -> List[str]:
            if not p:
                return words
            
            t = prefixes
            for c in p:
                if c not in t:
                    return []
                t = t[c]
            return [words[i] for i in t['#']]
        
        def backtrack() -> None:
            sn = len(square)
            if sn == n:
                ans.append(square[::])
            else:
                prefix = "".join([word[sn] for word in square])
                for word in getWords(prefix):
                    square.append(word)
                    backtrack()
                    square.pop()
        
        prefixes = {"#": []}
        for i, word in enumerate(words):
            p = prefixes
            for c in word:
                if c not in p:
                    p[c] = {'#': []}
                p = p[c]
                p['#'].append(i)
                
        n = len(words[0])
        ans = []
        square = []
        backtrack()
        return ans