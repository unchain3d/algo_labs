def left_ones(root):
    if not root:
        return 0

    if root.left and not root.left.left and not root.left.right:
        return root.left.value + left_ones(root.right)

    else:
        return left_ones(root.left) + left_ones(root.right)
