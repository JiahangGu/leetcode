#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 19:57
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        回溯算法，找到叶子结点并且路径和为给定数字的路径即可。
        :param root:
        :param sum:
        :return:
        """
        def dfs(current_root, current_sum, current_path):
            if current_root.left is None and current_root.right is None:
                if current_sum + current_root.val == sum:
                    current_path.append(current_root.val)
                    res.append(current_path[:])
                    current_path.pop()
                return
            current_sum += current_root.val
            current_path.append(current_root.val)
            if current_root.left is not None:
                dfs(current_root.left, current_sum, current_path)
            if current_root.right is not None:
                dfs(current_root.right, current_sum, current_path)
            current_sum -= current_root.val
            current_path.pop()

        if root is None:
            return []
        res = []
        dfs(root, 0, [])
        return res
