class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        ycounts = defaultdict(int)
        for x, y in points:
            ycounts[y] += 1
        
        total_lines = 0
        line_counts = []
        for y, count in ycounts.items():
            line_count = count * (count - 1) // 2
            line_counts.append(line_count)
            total_lines += line_count
        
        trap_count = 0
        remaining_lines = total_lines
        for i in range(len(line_counts) - 1):
            line_count = line_counts[i]
            remaining_lines -= line_count
            trap_count = (trap_count + line_count * remaining_lines) % MOD
        return trap_count

