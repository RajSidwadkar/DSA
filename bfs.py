from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfstreetraversal(root):
    if not root:
        return []
    
    queue = deque([root])
    res = []

    while queue:
        length = len(queue)
        currentlevel= []

        for i in range(length):
            node = queue.popleft()
            currentlevel.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(currentlevel)

    return res