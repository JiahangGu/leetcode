#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:24
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        """

        :param root:
        :return:
        """