class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        mapping = defaultdict(set)
        for w1, w2 in similarPairs:
            mapping[w1].add(w2)
            
        for i in range(len(sentence1)):
            if (
                sentence1[i] != sentence2[i] and 
                not sentence2[i] in mapping[sentence1[i]] and 
                not sentence1[i] in mapping[sentence2[i]]
            ):
                return False
        
        return True