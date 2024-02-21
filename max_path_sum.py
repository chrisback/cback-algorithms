class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, arr=None):
        # arr = [10, 2, 10, 20, 1, None, -25, None, None, None, None, None, None, 3, 4]

        arrp = arr if arr else []
        print(arrp)
        self.root: BinaryTreeNode = self._build_subtree(arrp, 0)
    
    def _build_subtree(self, arr: list[int], i: int) -> BinaryTreeNode | None:
        if i >= len(arr):
            return None
        
        print(f'{i+1}: {arr[i]}')

        if arr[i] is None:
            return None
        
        node = BinaryTreeNode(arr[i])
        node.left = self._build_subtree(arr, (((i+1)*2)-1))
        node.right = self._build_subtree(arr, ((i+1)*2))
        return node
    
    def _max_path_sum_helper(self, current_max: list[int | float], node: BinaryTreeNode) -> int:
        if node is None:
            return 0

        left_sum = self._max_path_sum_helper(current_max, node.left)
        right_sum = self._max_path_sum_helper(current_max, node.right)

        current_max[0] = max(current_max[0], left_sum + node.value + right_sum)
        return max(node.value, left_sum + node.value, right_sum + node.value)

    def max_path_sum(self):
        current_max = [float("-inf")]
        self._max_path_sum_helper(current_max, self.root)

        return current_max[0]
