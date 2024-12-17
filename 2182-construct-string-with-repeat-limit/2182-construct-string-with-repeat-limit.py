class RString(str):
    def __lt__(self, s):
        return self.__gt__(s)
        
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h = list(Counter(RString(c) for c in s).items())
        heapify(h)
        ans = []
        while h:
            ch, count = heappop(h)
            if count <= repeatLimit:
                ans.append(ch * count)
            else:
                ans.append(ch * repeatLimit)
                if not h:
                    break
                nch, ncount = heappop(h)
                ans.append(nch)
                if ncount - 1 > 0:
                    heappush(h, (nch, ncount - 1))
                heappush(h, (ch, count - repeatLimit))
        return "".join(ans)