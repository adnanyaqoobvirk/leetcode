class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        knows = deque([(1, 1)])
        knows_cnt = 1
        shares = deque()
        shares_cnt = 0

        for day in range(2, n + 1):
            if knows and day - delay >= knows[0][0]:
                kday, kcnt = knows.popleft()
                shares.append((kday, kcnt))
                shares_cnt += kcnt
                knows_cnt -= kcnt

            if shares and day - forget >= shares[0][0]:
                sday, scnt = shares.popleft()
                shares_cnt -= scnt

            if shares_cnt > 0:
                knows.append((day, shares_cnt))
                knows_cnt += shares_cnt

        return (knows_cnt + shares_cnt) % MOD
