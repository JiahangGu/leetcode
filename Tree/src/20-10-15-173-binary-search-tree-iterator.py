#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 9:40
# @Author:JiahangGu
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        """
        纠结了半天在next中O(h)空间和O(1)时间是怎么做到的，看了题解之后发现使用摊还分析之后，对于每个节点
        不存在右子节点和存在右子节点的复杂度平均下来确实是O(1)。因为理论上每个节点在入栈过程中最多访问一次。
        而next需要调用n次遍历。
        :param root:
        """
        self.stack = []
        self._inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self._inorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

    def _inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
