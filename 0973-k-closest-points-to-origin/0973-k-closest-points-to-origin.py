class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(l: int, r: int) -> int:
            if l >= r:
                return l
            
            p = randint(l, r)
            d[r], d[p] = d[p], d[r]

            i = l
            for j in range(l, r):
                if d[j][1] < d[r][1]:
                    d[i], d[j] = d[j], d[i]
                    i += 1
            d[i], d[r] = d[r], d[i]
            return i
        
        d = []
        for i, point in enumerate(points):
            d.append([i, point[0]**2 + point[1]**2])

        left, right = 0, len(points) - 1
        while True:
            pivot = partition(left, right)

            if pivot == k:
                ans = []
                for i in range(pivot):
                    ans.append(points[d[i][0]])
                return ans
            elif pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1