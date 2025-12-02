class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        ycounts = defaultdict(int)
        for x, y in points:
            ycounts[y] += 1
        
        total_lines = 0
        trap_count = 0
        for y, count in ycounts.items():
            line_count = count * (count - 1) // 2
            trap_count = (trap_count + line_count * total_lines) % MOD
            total_lines += line_count
        return trap_count

