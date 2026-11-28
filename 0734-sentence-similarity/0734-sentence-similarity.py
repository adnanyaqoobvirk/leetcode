class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        wordMap = defaultdict(set)
        for w1, w2 in similarPairs:
            wordMap[w1].add(w2)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2:
                if w2 not in wordMap[w1] and w1 not in wordMap[w2]:
                    return False
        return True