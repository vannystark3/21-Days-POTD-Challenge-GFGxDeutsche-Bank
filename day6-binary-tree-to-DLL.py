class Solution:
    def bToDLL(self, root):
        # Helper function for in-order traversal
        def inOrderTraversal(node):
            nonlocal head, prev
            
            if node is None:
                return
            
            # Recur on the left subtree
            inOrderTraversal(node.left)
            
            # If prev is None, this node is the head of the DLL
            if prev is None:
                head = node
            else:
                # Adjust pointers
                prev.right = node
                node.left = prev
            
            # Update prev to current node
            prev = node
            
            # Recur on the right subtree
            inOrderTraversal(node.right)
        
        # Initialize head and prev
        head = None
        prev = None
        
        # Convert binary tree to DLL
        inOrderTraversal(root)
        
        return head
