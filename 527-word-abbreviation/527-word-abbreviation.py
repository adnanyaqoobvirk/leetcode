class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        ans = {}
        abbrs = defaultdict(lambda: [1,[]])
        for word in words:
            if len(word) <= 3:
                abbr = word
            else:
                abbr = f"{word[0]}{len(word) - 2}{word[-1]}"
            abbrs[abbr][1].append(word)
            ans[word] = abbr
            
        stop = False
        while not stop:
            stop = True
            for abbr, (idx, awords) in list(abbrs.items()):
                if len(awords) > 1:
                    stop = False
                    
                    del abbrs[abbr]
                    
                    for word in awords:
                        if len(word) - idx - 2 < 2:
                            abbr = word
                        else:
                            abbr = f"{word[:idx + 1]}{len(word) - idx - 2}{word[-1]}"
                        abbrs[abbr][0] = idx + 1
                        abbrs[abbr][1].append(word)
                        ans[word] = abbr
        return [ans[word] for word in words]