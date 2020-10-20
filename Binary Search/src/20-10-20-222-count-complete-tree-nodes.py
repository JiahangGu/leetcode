#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 16:10
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        如果使用遍历的方法是线性时间复杂度，且没有使用这是一颗完全二叉树的条件。
        考虑到完全二叉树的特点：最后一层最后一个结点的左边结点全部存在，右边没有结点。所以如果可以找到最后一个结点则
        可以确定出最后一层的结点个数k，假设d层，则节点数为2**d + k - 1，d是从0开始算。
        首先求出树的深度d，则最后一层结点序号为0-2**(d-1)，使用二分算法查找最后一个结点。具体是根据序号和结点个数判断
        是在左子树还是右子树，然后进入最后一层判断该节点是否存在，从根节点开始进入depth层即是最后一层。
        :param root:
        :return:
        """
        def get_depth(root):
            depth = 0
            while root.left:
                depth += 1
                root = root.left
            return depth

        def exist(root, idx, depth):
            l, r = 0, 2 ** depth - 1
            for i in range(depth):
                mid = l + (r - l) // 2
                if idx <= mid:
                    root = root.left
                    r = mid
                else:
                    root = root.right
                    l = mid + 1
            return not root is None

        if not root:
            return 0
        depth = get_depth(root)
        if depth == 0:
            return 1
        l, r = 0, 2 ** depth - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if exist(root, mid, depth):
                l = mid
            else:
                r = mid - 1
        return 2 ** depth + l