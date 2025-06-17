"""
Approach:
- We use Kahn's Algorithm (BFS-based Topological Sort) to detect cycles in a directed graph.
- First, we build an adjacency list from prerequisites.
- Then, we compute the in-degree (number of prerequisites) for each course.
- We enqueue all courses with in-degree 0 (i.e., no prerequisites).
- While processing the queue, for each course taken, we reduce the in-degree of its dependent courses.
- If any of those reach in-degree 0, we enqueue them.
- If we can process all `numCourses`, return True (no cycle).
- If not, return False (cycle exists).

Time Complexity: O(V + E), where V = numCourses, E = number of prerequisites
Space Complexity: O(V + E), for the adjacency list and in-degree array
"""
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        if not queue:
            return False
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            for course in adj_list[curr]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return count == numCourses
    
    def main(self):
        # Test Case 1: No cycle → should return True
        numCourses = 6
        prerequisites = [
            [1, 0],
            [2, 0],
            [3, 1],
            [3, 2],
            [4, 2],
            [5, 3],
            [5, 4]
        ]
        print("Can finish all courses:", self.canFinish(numCourses, prerequisites))
        # Expected Output: True

        # Test Case 2: Has cycle → should return False
        numCourses = 3
        prerequisites = [
            [0, 1],
            [1, 2],
            [2, 0]
        ]
        print("Can finish all courses:", self.canFinish(numCourses, prerequisites))
        # Expected Output: False

# Run it
sol = Solution()
sol.main()