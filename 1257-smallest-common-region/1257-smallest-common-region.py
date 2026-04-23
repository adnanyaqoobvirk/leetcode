class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = defaultdict(str)
        for region in regions:
            parent = region[0]
            for i in range(1, len(region)):
                parents[region[i]] = parent
        
        region1_parents = set()
        parent = region1
        while parent != "":
            region1_parents.add(parent)
            parent = parents[parent]
        
        parent = region2
        while parent not in region1_parents:
            parent = parents[parent]
        
        return parent
