class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        trie = {}
        for i, p in enumerate(products):
            t = trie
            for c in p:
                if c not in t:
                    t[c] = {'$':[]}
                t = t[c]
                if len(t['$']) < 3:
                    t['$'].append(i)
        
        ans = []
        t = trie
        for i, c in enumerate(searchWord):
            if c not in t:
                for j in range(i, len(searchWord)):
                    ans.append([])
                break
            else:
                t = t[c]
                ss = []
                for j in t['$']:
                    ss.append(products[j])
                ans.append(ss)
        return ans