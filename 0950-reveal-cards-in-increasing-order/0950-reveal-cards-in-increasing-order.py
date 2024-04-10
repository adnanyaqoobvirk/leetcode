class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque(range(len(deck)))
        deck.sort()
        ans = [None] * len(deck)
        for v in deck:
            ans[q.popleft()] = v
            if q:
                q.append(q.popleft())
        return ans