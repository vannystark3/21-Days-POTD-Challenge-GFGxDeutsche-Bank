class Solution:
    def merge(self, root1, root2):
        def inorder_traversal(root):
            stack = []
            result = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.data)
                root = root.right
            return result

        def merge_sorted_arrays(arr1, arr2):
            merged = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            # Append remaining elements
            merged.extend(arr1[i:])
            merged.extend(arr2[j:])
            return merged

        # Get sorted elements from both BSTs
        sorted_bst1 = inorder_traversal(root1)
        sorted_bst2 = inorder_traversal(root2)

        # Merge the sorted arrays
        return merge_sorted_arrays(sorted_bst1, sorted_bst2)
