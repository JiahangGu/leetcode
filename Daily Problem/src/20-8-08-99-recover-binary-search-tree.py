#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:24
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        空间复杂度为O(n)的解法很简单，只需要中序遍历一次树，得到的序列和应该得到的升序序列做对比，
        即找到唯一的一个降序序列[i,j]，并在树中将nums[i], nums[j]对应的值互换位置即可。
        思路清晰，不再实现，考虑下空间复杂度为O(1)的解法。

        :param root:
        :return:
        """