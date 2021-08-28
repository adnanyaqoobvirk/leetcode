class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        destinations = set()
        for src, des in paths:
            sources.add(src)
            destinations.add(des)
            if des in sources:
                destinations.remove(des)
            if src in destinations:
                destinations.remove(src)
        return next(iter(destinations))