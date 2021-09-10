class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label >= 1:
            ans.append(label)
            lvl = int(math.log(label, 2))
            lvl_max = 1 << lvl + 1
            label = (lvl_max - (1 << lvl) + lvl_max - label - 1) // 2
        return ans[::-1]
                