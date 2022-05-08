class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, indegrees = defaultdict(list), defaultdict(int)
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                first_char = words[i][j]
                second_char = words[i + 1][j] if j < len(words[i + 1]) else ""
                if first_char != second_char:
                    graph[first_char].append(second_char)
                    indegrees[second_char] += 1
                    break
                
        unique_chars = {c for word in words for c in word}
        q, ans = [c for c in unique_chars if indegrees[c] == 0], []
        while q:
            nq = []
            for src in q:
                ans.append(src)
                for dst in graph[src]:
                    indegrees[dst] -= 1
                    if indegrees[dst] == 0:
                        nq.append(dst)
            q = nq
        return "" if len(ans) != len(unique_chars) else "".join(ans)
                