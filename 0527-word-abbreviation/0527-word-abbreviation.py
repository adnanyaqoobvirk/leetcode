class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        groups = defaultdict(list)
        for word in words:
            groups[word[0] + str(len(word)) + word[-1]].append(word)
        
        ans = {}
        for group in groups.values():
            if len(group[0]) <= 3:
                for word in group:
                    ans[word] = word
                continue

            if len(group) == 1:
                word = group[0]
                ans[word] = f"{word[0]}{len(word) - 2}{word[-1]}"
                continue
            
            trie = {"$": 0}
            for word in group:
                start = word[0] + word[-1]
                if start not in trie:
                    trie[start] = {"$": 0}
                trie[start]["$"] += 1
                t = trie[start]
                for c in word[1:len(word) - 1]:
                    if c not in t:
                        t[c] = {"$": 0}
                    t = t[c]
                    t["$"] += 1
            
            for word in group:
                start = word[0] + word[-1]
                t = trie[start]
                count = 0
                for c in word[1:len(word) - 1]:
                    t = t[c]
                    if t["$"] <= 1:
                        break
                    count += 1

                if len(word) - 3 - count <= 1:
                    ans[word] = word
                else:
                    ans[word] = f"{word[:count + 2]}{len(word) - 3 - count}{word[-1]}"
                
        return [ans[word] for word in words]
