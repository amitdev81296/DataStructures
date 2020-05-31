from .tree import Tree


def sum_tree_elements(my_tree):
    if my_tree == None:
        return 0
    return sum_tree_elements(my_tree.left) + sum_tree_elements(my_tree.right) + my_tree.cargo


my_tree = Tree(3, Tree(2, Tree(1), Tree(4)), Tree(5, Tree(6), Tree(7)))
sum_result = sum_tree_elements(my_tree)
print("\nTree Element Addition Result : ", str(sum_result), "\n")

