class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        
       # Initialize a TreeNode with a value and optional left and right children.
        
        self.value = value
        self.left = left
        self.right = right

def max_depth(root):
    """
    Calculate the maximum depth of the binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The maximum depth of the binary tree.
    """
    if root is None:
        return 0
    else:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        return max(left_depth, right_depth) + 1

# Example Usage
if __name__ == "__main__":
    # Constructing an example tree:
    #        Q1
    #       /  \
    #     Q2    Q3
    #    / \   / \
    #  Q4  Q5 Q6  Q7

    root = TreeNode("Q1")
    root.left = TreeNode("Q2")
    root.right = TreeNode("Q3")
    root.left.left = TreeNode("Q4")
    root.left.right = TreeNode("Q5")
    root.right.left = TreeNode("Q6")
    root.right.right = TreeNode("Q7")

    print("Maximum Depth:", max_depth(root))  # Output: 3
