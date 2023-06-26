class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        mapping = defaultdict(set)
        for w1, w2 in similarPairs:
            mapping[w1].add(w2)
            mapping[w2].add(w1)
            
        for i in range(len(sentence1)):
            mapping[sentence1[i]].add(sentence1[i])
            if not sentence2[i] in mapping[sentence1[i]]:
                return False
        
        return True