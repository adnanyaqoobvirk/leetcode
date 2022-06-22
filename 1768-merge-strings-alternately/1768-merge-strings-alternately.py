class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(
            c1 + c2 
            for c1, c2 in itertools.zip_longest(
                word1, word2, fillvalue=''
            )
        )