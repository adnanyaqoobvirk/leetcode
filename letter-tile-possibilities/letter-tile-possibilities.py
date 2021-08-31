class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(t: List[int], chars: List[str]) -> None:
            if chars:
                combs.add("".join(chars))
            
            for i in range(len(t)):
                chars.append(t[i])
                backtrack(t[:i] + t[i + 1:], chars)
                chars.pop()
        
        n = len(tiles)
        combs = set()
        backtrack(tiles, [])
        return len(combs)