class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        path = set()
        visited = set()

        def dfs(course):

            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True