#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 14:52
# @Author:JiahangGu
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        回溯法。使用DFS遍历从根节点到叶子结点，并记录当前路径对应值，传入下一层递归的参数是num*10+cur.val，
        并使用全局变量ans在到达叶结点时计算和。
        :param root:
        :return:
        """
        if root is None:
            return 0

        def get_sum(root, cur_val):
            if root.left is None and root.right is None:
                return cur_val * 10 + root.val
            ans = 0
            if root.left is not None:
                ans += get_sum(root.left, cur_val * 10 + root.val)
            if root.right is not None:
                ans += get_sum(root.right, cur_val * 10 + root.val)
            return ans

        ans = get_sum(root, 0)
        return ans
