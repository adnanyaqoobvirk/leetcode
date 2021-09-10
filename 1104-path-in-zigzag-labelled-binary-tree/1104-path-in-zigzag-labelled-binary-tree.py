class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = deque()
        lvl = int(math.log(label, 2)) + 1
        while label >= 1:
            ans.appendleft(label)
            label = ((1 << lvl) + (1 << lvl - 1) - label - 1) // 2
            lvl -= 1
        return ans
                