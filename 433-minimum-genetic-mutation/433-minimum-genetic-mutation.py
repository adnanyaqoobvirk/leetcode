class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        MAX_MUTATION_LENGTH, GENE_CHARS = 8, "ACGT"
        q, bank, mutations, seen = [start], set(bank), 0, {start}
        while q:
            nq = []
            for m in q:
                if m == end:
                    return mutations
                for i in range(MAX_MUTATION_LENGTH):
                    for c in GENE_CHARS:
                        nm = f"{m[0:i]}{c}{m[i+1:]}"
                        if nm not in seen and nm in bank:
                            seen.add(nm)
                            nq.append(nm)
            q = nq
            mutations += 1
        return -1