class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t_ops = b_ops = 0
        for i in range(1, len(tops)):
            if t_ops != float('inf') and tops[i] != tops[0]: 
                if bottoms[i] == tops[0]:
                    t_ops += 1
                else:
                    t_ops = float('inf')
            
            if b_ops != float('inf') and bottoms[i] != bottoms[0]:
                if tops[i] == bottoms[0]:
                    b_ops += 1
                else:
                    b_ops = float('inf')
        
        ans = min(t_ops, b_ops)
        t_ops = b_ops = 0
        for i in range(len(tops)):
            if t_ops != float('inf') and bottoms[i] != tops[0]: 
                if tops[i] == tops[0]:
                    t_ops += 1
                else:
                    t_ops = float('inf')
            
            if b_ops != float('inf') and tops[i] != bottoms[0]:
                if bottoms[i] == bottoms[0]:
                    b_ops += 1
                else:
                    b_ops = float('inf')
        ans = min(t_ops, b_ops, ans)
        return ans if ans != float('inf') else -1
                