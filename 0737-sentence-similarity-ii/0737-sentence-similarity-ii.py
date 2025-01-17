class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], sp: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False
        
        def find(w: str) -> int:
            if uf[w] != w:
                uf[w] = find(uf[w])
            return uf[w]
        
        def union(w1: str, w2: str):
            p1, p2 = find(w1), find(w2)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    uf[p2] = p1
                else:
                    uf[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p2] += 1
        
        uf = {}
        rank = defaultdict(int)
        for word1, word2 in sp:
            if word1 not in uf:
                uf[word1] = word1
            if word2 not in uf:
                uf[word2] = word2
            union(word1, word2)
        
        for word1, word2 in zip(s1, s2):
            if word1 == word2:
                continue
            if word1 not in uf or word2 not in uf or find(word1) != find(word2):
                return False
        
        return True