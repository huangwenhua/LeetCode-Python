from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        encoded = []

        self.preorder(root, encoded)

        return ','.join([str(x) for x in encoded])

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        decoded = list(map(lambda x: int(x), data.split(',')))

        return self.build_tree(decoded, 0, len(decoded) - 1)

    def preorder(self, root: TreeNode, encoded: List[str]) -> None:
        if not root:
            return

        encoded.append(root.val)

        self.preorder(root.left, encoded)
        self.preorder(root.right, encoded)

    def build_tree(self, preorder: List[int], start: int, end: int) \
            -> TreeNode:
        if start > end:
            return None

        root_value = preorder[start]
        right_tree_start = next(
            (i for i in range(start, end + 1) if preorder[i] > root_value),
            end + 1)

        root = TreeNode(root_value)
        root.left = self.build_tree(preorder, start + 1, right_tree_start - 1)
        root.right = self.build_tree(preorder, right_tree_start, end)

        return root
