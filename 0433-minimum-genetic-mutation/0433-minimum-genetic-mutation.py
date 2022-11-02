class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        choices = "ACGT"
        bank_set = set(bank)
        seen = {start}
        q = [start]
        mutations = 0
        while q:
            nq = []
            for m in q:
                if m == end:
                    return mutations
                for i in range(8):
                    for c in choices:
                        nm = f"{m[:i]}{c}{m[i + 1:]}"
                        if nm in bank_set and nm not in seen:
                            seen.add(nm)
                            nq.append(nm)
            mutations += 1
            q = nq
        return -1