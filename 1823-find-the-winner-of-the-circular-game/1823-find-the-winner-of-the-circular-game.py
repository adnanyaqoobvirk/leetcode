class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        pos = 0
        for i in range(n - 1):
            pos = (pos + k - 1) % len(friends)
            friends.pop(pos)
        return friends[0]