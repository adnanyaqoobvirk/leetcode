class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(t: set[int], chars: List[str]) -> None:
            if chars:
                combs.add("".join(chars))
            
            if len(t) < n:
                for i in range(len(tiles)):
                    if i not in t:
                        chars.append(tiles[i])
                        t.add(i)
                        backtrack(t, chars)
                        t.remove(i)
                        chars.pop()
        
        n = len(tiles)
        combs = set()
        backtrack(set(), [])
        return len(combs)