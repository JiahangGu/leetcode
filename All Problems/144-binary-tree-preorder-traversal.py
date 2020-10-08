#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/8 9:02
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        前序遍历，一路向左的路上记录根节点的值，并放入栈等待后续回溯。当左子节点为空时，弹出栈作为当前结点
        ，即进入回溯过程，并进入右子节点。因为结点为空时会直接弹出栈作为当前结点，所以右子节点是否为空不影响。
        :param root:
        :return:
        """
        # stack = []
        # ans = []
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         ans.append(root.val)
        #         root = root.left
        #     root = stack.pop()
        #     root = root.right
        # return ans
        """
        另一种方式是用栈模拟访问顺序，既然要先左后右，那么放入栈选择先右后左即可。
        """
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
