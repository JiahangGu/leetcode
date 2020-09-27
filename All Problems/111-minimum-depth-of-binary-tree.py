#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/21 14:31
# @Author:JiahangGu

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        最小深度就是左右子树的最小深度+1.需要注意的是如果某个非叶子节点的某个子树是null，则
        null子树不计入计算，因为这个节点不是叶子节点，不符合题目要求，只有子树存在的情况下
        应该计算
        :param root:
        :return:
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        min_depth = 10 ** 8
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        return min_depth + 1