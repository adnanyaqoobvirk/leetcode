class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, prev, currWidth = [], 0, len(words[0])
        for curr in range(1, len(words)):
            if currWidth + len(words[curr]) + (curr - prev) > maxWidth:
                spaces = maxWidth - currWidth
                extraSpaces = 0
                if curr - prev > 1:
                    spaces = (maxWidth - currWidth) // (curr - prev - 1)
                    extraSpaces = (maxWidth - currWidth) % (curr - prev - 1)
                line, lineWidth = [], 0
                for i in range(prev, curr):
                    line.append(words[i])
                    lineWidth += len(words[i])
                    for _ in range(spaces):
                        if lineWidth < maxWidth:
                            line.append(" ")
                            lineWidth += 1
                    if extraSpaces > 0 and lineWidth < maxWidth:
                        line.append(" ")
                        lineWidth += 1
                        extraSpaces -= 1
                res.append(line)
                currWidth = 0
                prev = curr
            currWidth += len(words[curr])
            
        line, lineWidth = [], 0
        for curr in range(prev, len(words)):
            line.append(words[curr])
            lineWidth += len(words[curr])
            if lineWidth < maxWidth:
                line.append(" ")
                lineWidth += 1
                
        for _ in range(lineWidth, maxWidth):
            line.append(" ")
        
        res.append(line)
        
        return ["".join(line) for line in res]