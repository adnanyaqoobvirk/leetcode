class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack():
            if len(comb) == n:
                bs = "".join(comb)
                if bs not in invalid:
                    return bs
            else:
                if counts[len(comb)] == n:
                    comb.append("0")
                    bs = backtrack()
                    if bs:
                        return bs
                    comb.pop()
                elif counts[len(comb)] == -n:
                    comb.append("1")
                    bs = backtrack()
                    if bs:
                        return bs
                    comb.pop()
                else:
                    comb.append("1")
                    bs = backtrack()
                    if bs:
                        return bs
                    comb.pop()
                    comb.append("0")
                    bs = backtrack()
                    if bs:
                        return bs
                    comb.pop()
            return ""

        n = len(nums)
        counts = [0] * n
        for num in nums:
            for i, d in enumerate(num):
                if d == "0":
                    counts[i] -= 1
                else:
                    counts[i] += 1
        comb = []
        invalid = set(nums)
        return backtrack()