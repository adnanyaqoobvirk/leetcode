class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        kt = tickets[k] - 1
        for t in tickets:
            ans += min(t, kt)
        for i in range(k + 1):
            if tickets[i] >= tickets[k]:
                ans += 1
        return ans