class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aseen = set()
        bseen = set()
        common = set()
        ans = []
        for i in range(len(A)):
            aseen.add(A[i])
            bseen.add(B[i])

            if B[i] in aseen:
                common.add(B[i])
            
            if A[i] in bseen:
                common.add(A[i])
            
            ans.append(len(common))
        return ans