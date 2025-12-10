class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        complexity_counts = Counter(complexity)
        min_complexity = min(complexity)
        if min_complexity != complexity[0] or complexity_counts[min_complexity] > 1:
            return 0
        
        MOD = 10**9 + 7
        permutation_count = 1
        for i in range(1, len(complexity)):
            permutation_count = (permutation_count * i) % MOD
        return permutation_count