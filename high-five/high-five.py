class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        
        res = []
        prev_id = id_sum = id_count = 0
        for i, score in items:
            id_count += 1
            id_sum += score
            if prev_id != i:
                prev_id = i
                id_sum = score
                id_count = 1
            elif id_count == 5:
                res.append([i, id_sum // 5])
        return res
                