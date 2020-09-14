#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 9:22
# @Author:JiahangGu
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代解法：和递归解法类似，首先左子树走到底直到不存在，并使用栈保存路径上的节点，在进入到最左之后，按照递归的解法，返回后
        进入下一步即mid，在迭代中还需要置当前节点的left为None，因为在下一次进入左子树的循环时会重复进入，而这在递归解法中时不需要
        注意的。最后如果存在right节点，和递归解法一样，进入到该节点并且继续遍历。在上述过程中，所以递归进入节点均采用入栈操作模拟
        :param root:
        :return:
        """
        if not root:
            return []
        stack = [root]
        cur = root
        ans = []
        while stack:
            while cur.left:
                stack.append(cur.left)
            cur = stack.pop()
            ans.append(cur.val)
            cur.left = None
            if cur.right:
                stack.append(cur.right)
                cur = cur.right
        return ans