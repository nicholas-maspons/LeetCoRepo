# 210. Course Schedule II

from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            if prerequisite not in graph:
                graph[prerequisite] = []
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            if course in graph:
                for next_course in graph[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)

        if len(order) == numCourses:
            return order
        else:
            return []
