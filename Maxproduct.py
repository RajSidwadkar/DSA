class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

subtree_sums = []

def calculateSum(node):
    if not node:
        return 0
    
    left_sum = calculateSum(node.left)
    right_sum = calculateSum(node.right)
    
    current_sum = node.val + left_sum + right_sum
    subtree_sums.append(current_sum)
    
    return current_sum

total_tree_sum = calculateSum(root)

max_product = 0
for s in subtree_sums:
    product = s * (total_tree_sum - s)
    if product > max_product:
        max_product = product

final_result = max_product % (10**9 + 7)

print(f"Subtree sums: {subtree_sums}")
print(f"Total sum: {total_tree_sum}")
print(f"Max Product: {final_result}")