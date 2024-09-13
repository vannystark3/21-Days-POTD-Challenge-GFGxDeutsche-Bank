class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,node):
        # Code here
        if node is None:
            return
        node.left,node.right = node.right,node.left
        self.mirror(node.left)
        self.mirror(node.right)
