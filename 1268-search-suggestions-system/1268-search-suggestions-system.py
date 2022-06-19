class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def search(lo: int, hi: int, j: int) -> Tuple[int, int]:
            if hi < lo:
                return lo, hi
            
            l, r = lo, hi
            while l < r:
                mid = l + (r - l) // 2
                if j < len(products[mid]) and products[mid][j] >= searchWord[j]:
                    r = mid
                else:
                    l = mid + 1
            
            lo = l
            
            l, r = lo, hi
            while l < r:
                mid = l + (r - l) // 2
                if j < len(products[mid]) and products[mid][j] <= searchWord[j]:
                    l = mid + 1
                else:
                    r = mid
            hi = l if j < len(products[l]) and products[l][j] == searchWord[j] else l - 1
            
            return lo, hi
        
        products.sort()
        
        ans, left, right = [], 0, len(products) - 1
        for i in range(len(searchWord)):
            left, right = search(left, right, i)
            
            ss = []
            for k in range(left, right + 1):
                if len(ss) == 3:
                    break
                ss.append(products[k])
            ans.append(ss)
        return ans