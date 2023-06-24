class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        imap = defaultdict(list)
        for i, c in enumerate(source):
            imap[c].append(i)
            
        scount, spos = 1, -1
        for c in target:
            ilist = imap[c]
            
            if not ilist:
                return -1
            
            l, h = -1, len(ilist) - 1
            while l + 1 < h:
                m = (l + h) >> 1
                
                if ilist[m] > spos:
                    h = m
                else:
                    l = m
            if ilist[h] <= spos:
                scount += 1
                spos = ilist[0]
            else:
                spos = ilist[h]
        return scount
        