#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 19:52
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        和利用前序和中序遍历建树思想一样，找根，划分左右子树，建树。
        后续遍历序列的最后一位是根节点。
        :param inorder:
        :param postorder:
        :return:
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        left = self.buildTree(inorder[:index], postorder[:index])
        right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        root.left = left
        root.right = right
        return root
