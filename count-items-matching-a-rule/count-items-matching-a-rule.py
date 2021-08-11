class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for t, c, n in items:
            if ruleKey == 'type':
                value = t
            elif ruleKey == 'color':
                value = c
            else:
                value = n
            
            if value == ruleValue:
                count += 1
        return count