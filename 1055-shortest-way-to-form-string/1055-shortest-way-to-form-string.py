class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idx_map = defaultdict(list)
        for i, c in enumerate(source):
            idx_map[c].append(i)
        
        ss_count = 1
        prev_idx = -1
        for c in target:
            char_indices = idx_map[c]
            
            if not char_indices:
                return -1

            lo, hi = -1, len(char_indices) - 1
            while lo + 1 < hi:
                mid = lo + hi >> 1
                if char_indices[mid] > prev_idx:
                    hi = mid
                else:
                    lo = mid
            if char_indices[hi] <= prev_idx:
                ss_count += 1
                prev_idx = char_indices[0]
            else:
                prev_idx = char_indices[hi]
        return ss_count