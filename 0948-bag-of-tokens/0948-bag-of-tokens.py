class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif l < r and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return score