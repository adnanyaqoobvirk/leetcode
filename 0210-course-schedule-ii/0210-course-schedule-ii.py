class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course: int) -> bool:
            visiting.add(course)
            processed.add(course)
            
            for nei in adj[course]:
                if nei in visiting:
                    return False
                if nei in processed:
                    continue
                if not dfs(nei):
                    return False

            visiting.remove(course)
            ordered_courses.append(course)
            return True
        
        adj = defaultdict(list)
        for dst, src in prerequisites:
            adj[dst].append(src)
        
        visiting = set()
        processed = set()
        ordered_courses = []
        unprocessed_courses = set(range(numCourses))
        while unprocessed_courses:
            course = unprocessed_courses.pop()
            if course in processed:
                continue
            if not dfs(course):
                return []
        
        return ordered_courses