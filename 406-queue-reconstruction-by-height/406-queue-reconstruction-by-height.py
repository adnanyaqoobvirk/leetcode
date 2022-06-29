class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[1], x[0]))
        
        ans = []
        for h, k in people:
            ck = k
            i = -1
            for i in range(len(ans)):
                if ans[i][0] < h:
                    continue
                else:
                    ck -= 1
                if ck < 0:
                    ans.insert(i, [h, k])
                    break
            else:
                ans.insert(i + 1, [h, k])
        return ans