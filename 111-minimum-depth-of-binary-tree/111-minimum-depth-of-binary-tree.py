from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: An empty tree has 0 depth.
        if not root:
            return 0
        
        # Use a queue to store (node, current_depth)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if this is a leaf node
            if not node.left and not node.right:
                # This is the first leaf we've found, so it's the minimum depth.
                return depth
            
            # If not a leaf, add its children to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))