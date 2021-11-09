class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ans = []
        wmasks = defaultdict(int)
        for word in words:
            wmask = 0
            for c in word:
                wmask |= (1 << ord(c) - ord('a'))
            wmasks[wmask] += 1
        
        for puzzle in puzzles:
            pmask = 0
            for c in puzzle[1:]:
                pmask |= (1 << ord(c) - ord('a'))
            
            fmask = 1 << ord(puzzle[0]) - ord('a')
            valids = wmasks[fmask]
            subset = pmask
            while subset:
                valids += wmasks[subset | fmask]
                subset = (subset - 1) & pmask
            ans.append(valids)
        return ans