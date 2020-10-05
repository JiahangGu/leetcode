#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 19:46
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        只要找到根节点就可以建树。前序序列的第一个元素是根节点，然后从中序中找到该位置，以这个位置为划分，
        左边是左子树，右边是右子树，对应建树。
        :param preorder:
        :param inorder:
        :return:
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
                break
        left = self.buildTree(preorder[1:index + 1], inorder[:index])
        right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        root.left = left
        root.right = right
        return root
