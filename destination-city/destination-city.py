class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        destinations = set()
        for src, des in paths:
            sources.add(src)
            destinations.add(des)
        return next(iter(destinations - sources))