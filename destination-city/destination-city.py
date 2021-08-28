class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return next(iter({des for _, des in paths} - {src for src, _ in paths}))