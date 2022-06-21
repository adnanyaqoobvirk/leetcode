class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        ans = [""] * len(words)
        abbrs = defaultdict(lambda: [1,[]])
        for i, word in enumerate(words):
            if len(word) <= 3:
                abbr = word
            else:
                abbr = f"{word[0]}{len(word) - 2}{word[-1]}"
            abbrs[abbr][1].append(i)
            ans[i] = abbr
            
        stop = False
        while not stop:
            stop = True
            for abbr, (idx, awords) in list(abbrs.items()):
                if len(awords) > 1:
                    stop = False
                    
                    del abbrs[abbr]
                    
                    for i in awords:
                        word = words[i]
                        if len(word) - idx - 2 < 2:
                            abbr = word
                        else:
                            abbr = f"{word[:idx + 1]}{len(word) - idx - 2}{word[-1]}"
                        abbrs[abbr][0] = idx + 1
                        abbrs[abbr][1].append(i)
                        ans[i] = abbr
        return ans