class Tree:
    
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.cargo)

traversal_array = []

def sum_tree_elements(my_tree):
    if my_tree == None:
        return 0
    return sum_tree_elements(my_tree.left) + sum_tree_elements(my_tree.right) + my_tree.cargo


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        traversal_array.append(root.cargo)
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        traversal_array.append(root.cargo)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        traversal_array.append(root.cargo)


my_tree = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
sum_result = sum_tree_elements(my_tree)
print("\nTree Element Addition Result : ", str(sum_result))
print("\n*****TreeTraversal*****")
print("1. Inorder Traversal")
inorder_traversal(my_tree)
print(traversal_array)
traversal_array = []
print("\n2. Preorder Traversal")
preorder_traversal(my_tree)
print(traversal_array)
traversal_array = []
print("\n3. Postorder Traversal")
postorder_traversal(my_tree)
print(traversal_array)
traversal_array = []
