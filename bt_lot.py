###
# Approach:
# We use BFS with a queue to traverse the tree level by level.
# For each level, we process all nodes currently in the queue (i.e., one full level),
# add their values to a result list, and enqueue their children.
#
# Time Complexity: O(n), where n is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(n), for the queue and result list
###

from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = 0
        result = []
        while queue:
            result.append([])
            for i in range(len(queue)):
                curr = queue.popleft()
                result[level].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return result
    
    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        result = self.levelOrder(root)
        print("Level Order Traversal:", result)
        root2 = TreeNode(3)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)
        print("Level Order Traversal (Tree 2):", self.levelOrder(root2))

sol = Solution()
sol.main()