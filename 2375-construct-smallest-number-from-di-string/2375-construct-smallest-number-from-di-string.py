class Solution:
    def smallestNumber(self, pattern: str) -> str:
        dcount = 0
        digit = 0
        res = []
        for c in chain(pattern, "I"):
            if c == "I":
                if dcount > 0:
                    for i in reversed(range(1, dcount + 2)):
                        res.append(str(digit + i))
                    digit += dcount + 1
                    dcount = 0
                else:
                    digit += 1
                    res.append(str(digit))
            else:
                dcount += 1
        return "".join(res)