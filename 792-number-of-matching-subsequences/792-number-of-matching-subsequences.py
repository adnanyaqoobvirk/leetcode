class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            itr = iter(word)
            buckets[next(itr)].append(itr)
        
        ans = 0
        for c in s:
            b = buckets[c]
            buckets[c] = []
            
            for itr in b:
                nitr = next(itr, None)
                if nitr:
                    buckets[nitr].append(itr)
                else:
                    ans += 1
        return ans