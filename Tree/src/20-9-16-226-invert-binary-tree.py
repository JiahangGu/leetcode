#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/16 13:12
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归反转，当前节点root的左右子节点互换，然后分别进入到左右子树进行互换
        :param root:
        :return:
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root