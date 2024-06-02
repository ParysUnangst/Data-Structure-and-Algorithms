from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        
        # Initialize a TreeNode with a value and optional left and right children.
        
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    
    # Traverse the tree in preorder (Root, Left, Right) and return the values as a list.
    
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    
    # Traverse the tree in order (Left, Root, Right) and return the values as a list.
    
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def postorder_traversal(root):
    
    # Traverse the tree in postorder (Left, Right, Root) and return the values as a list.
    
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

def level_order_traversal(root):
    
    # Traverse the tree in level order (Breadth-First Search) and return the values as a list.
    
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def build_tree_pre_in(preorder, inorder):
    
   # Build a binary tree given the preorder and inorder traversal lists.
    
    if not preorder or not inorder:
        return None
    
    root_value = preorder.pop(0)
    root = TreeNode(root_value)
    
    inorder_index = inorder.index(root_value)
    
    root.left = build_tree_pre_in(preorder, inorder[:inorder_index])
    root.right = build_tree_pre_in(preorder, inorder[inorder_index + 1:])
    
    return root

def build_tree_in_post(inorder, postorder):
    
    # Build a binary tree given the inorder and postorder traversal lists.
    
    if not inorder or not postorder:
        return None
    
    root_value = postorder.pop()
    root = TreeNode(root_value)
    
    inorder_index = inorder.index(root_value)
    
    root.right = build_tree_in_post(inorder[inorder_index + 1:], postorder)
    root.left = build_tree_in_post(inorder[:inorder_index], postorder)
    
    return root

# Test Cases
if __name__ == "__main__":
    # Simple Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Simple Tree")
    print("Preorder:", preorder_traversal(root))  # [1, 2, 3]
    print("Inorder:", inorder_traversal(root))   # [2, 1, 3]
    print("Postorder:", postorder_traversal(root)) # [2, 3, 1]
    print("Level Order:", level_order_traversal(root)) # [1, 2, 3]

    # Larger Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("\nLarger Tree")
    print("Preorder:", preorder_traversal(root))  # [1, 2, 4, 5, 3]
    print("Inorder:", inorder_traversal(root))   # [4, 2, 5, 1, 3]
    print("Postorder:", postorder_traversal(root)) # [4, 5, 2, 3, 1]
    print("Level Order:", level_order_traversal(root)) # [1, 2, 3, 4, 5]

    # Empty Tree
    root = None

    print("\nEmpty Tree")
    print("Preorder:", preorder_traversal(root))  # []
    print("Inorder:", inorder_traversal(root))   # []
    print("Postorder:", postorder_traversal(root)) # []
    print("Level Order:", level_order_traversal(root)) # []

    # Skewed Tree (Left)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)

    print("\nSkewed Tree (Left)")
    print("Preorder:", preorder_traversal(root))  # [1, 2, 3]
    print("Inorder:", inorder_traversal(root))   # [3, 2, 1]
    print("Postorder:", postorder_traversal(root)) # [3, 2, 1]
    print("Level Order:", level_order_traversal(root)) # [1, 2, 3]

    # Constructing Trees
    preorder = [1, 2, 4, 5, 3]
    inorder = [4, 2, 5, 1, 3]
    postorder = [4, 5, 2, 3, 1]

    constructed_tree_pre_in = build_tree_pre_in(preorder.copy(), inorder.copy())
    constructed_tree_in_post = build_tree_in_post(inorder.copy(), postorder.copy())

    print("\nConstructed Tree from Preorder and Inorder")
    print("Preorder:", preorder_traversal(constructed_tree_pre_in))  # Should match the original preorder list
    print("Inorder:", inorder_traversal(constructed_tree_pre_in))    # Should match the original inorder list

    print("\nConstructed Tree from Inorder and Postorder")
    print("Inorder:", inorder_traversal(constructed_tree_in_post))    # Should match the original inorder list
    print("Postorder:", postorder_traversal(constructed_tree_in_post)) # Should match the original postorder list
