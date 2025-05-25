class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        @cache
        def dp(i: int, j: int, pmask: int, cmask: int) -> int:
            if i == m:
                return 0
            if j == n:
                return dp(i + 1, 0, cmask, 0)
            
            valid = seats[i][j] != "#"
            if i - 1 >= 0:
                if j - 1 >= 0 and seats[i - 1][j - 1] == "$":
                    valid = False
                if j + 1 < n and seats[i - 1][j + 1] == "$":
                    valid = False
            if j - 1 >= 0 and seats[i][j - 1] == "$":
                valid = False
            if j + 1 < n and seats[i][j + 1] == "$":
                valid = False
            
            ans = 0
            if valid:
                seats[i][j] = "$"
                ans = max(ans, 1 + dp(i, j + 1, pmask, cmask | (1 << j)))
                seats[i][j] = "."
            ans = max(ans, dp(i, j + 1, pmask, cmask))
        
            return ans
        m, n = len(seats), len(seats[0])
        return dp(0, 0, 0, 0)