class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24) <= 0.1
        
        ncards = cards[::]
        for i in range(len(cards)):
            for j in range(len(cards)):
                if i == j:
                    continue

                ncards.remove(cards[i])
                ncards.remove(cards[j])

                for op in ["+", "-", "*", "/"]:
                    if op == "+":
                        ncards.append(cards[i] + cards[j])
                    elif op == "-":
                        ncards.append(cards[i] - cards[j])
                    elif op == "*":
                        ncards.append(cards[i] * cards[j])
                    else:
                        if cards[j] == 0:
                            continue
                        ncards.append(cards[i] / cards[j])

                    if self.judgePoint24(ncards):
                        return True

                    ncards.pop()

                ncards.append(cards[i])
                ncards.append(cards[j])
        return False