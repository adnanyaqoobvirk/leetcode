class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        A, E, I, O, U = 0, 1, 2, 3, 4
        
        prev, curr = [1] * 5, [0] * 5
        for _ in range(n - 1):
            for pchar in range(5):
                if pchar == A:
                    curr[pchar] = prev[E]
                elif pchar == E:
                    curr[pchar] = (prev[A] + prev[I]) % MOD
                elif pchar == I:
                    curr[pchar] = sum(prev[ch] for ch in [0,1,3,4]) % MOD
                elif pchar == O:
                    curr[pchar] = (prev[I] + prev[U]) % MOD
                elif pchar == U:
                    curr[pchar] = prev[A]
            prev, curr = curr, prev
        return sum(prev) % MOD
        