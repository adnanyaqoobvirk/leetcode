class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def helper(t: Dict[str, int], has_first: int) -> int:
            valids = t['#'] if has_first else 0
            for c in puzzle:
                if c in t:
                    valids += helper(t[c], has_first or c == puzzle[0])
            return valids
            
        trie = {'#': 0}
        for word in words:
            word = set(word)
            if len(word) <= 7:
                t = trie
                for c in sorted(word):
                    if c not in t:
                        t[c] = {"#": 0}
                    t = t[c]
                t['#'] += 1
                
        ans = []
        for puzzle in puzzles:
            ans.append(helper(trie, False))
        return ans