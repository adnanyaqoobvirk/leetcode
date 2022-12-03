class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        for count, ch in sorted((-cnt, c) for c, cnt in Counter(s).items()):
            ans.append(ch * -count)
        return "".join(ans)