class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def distance(c1: str, c2: str) -> int:
            diff = ord(c1) - ord(c2)
            return 26 + diff if diff < 0 else diff
        
        def same(x: int, y: int) -> bool:
            if len(strings[i]) != len(strings[j]):
                return False
            
            d = distance(strings[x][0], strings[y][0])
            for k in range(1, len(strings[i])):
                if distance(strings[i][k], strings[j][k]) != d:
                    return False
            return True
                    
        n = len(strings)
        ans = []
        done = set()
        for i in range(n):
            if i not in done:
                done.add(i)
                group = [strings[i]]
                for j in range(i + 1, n):
                    if j not in done and same(i, j):
                        done.add(j)
                        group.append(strings[j])
                ans.append(group)
        return ans