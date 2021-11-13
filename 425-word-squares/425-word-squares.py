class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack() -> None:
            sn = len(square)
            if sn == n:
                ans.append(square[::])
            else:
                prefix = "".join([word[sn] for word in square])
                for word in prefixes[prefix]:
                    square.append(word)
                    backtrack()
                    square.pop()
        
        prefixes = defaultdict(list)
        prefixes[""] = words
        for word in words:
            prefix = ""
            for c in word:
                prefix += c
                prefixes[prefix].append(word)
                
        n = len(words[0])
        ans = []
        square = []
        backtrack()
        return ans