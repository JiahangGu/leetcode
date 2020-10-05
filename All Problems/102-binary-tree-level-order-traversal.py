#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 17:01
# @Author:JiahangGu
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        使用队列来模拟，并且记录下一层的元素个数。具体做法是：初始队列为[root]，第一层结点个数为1，
        当前层剩余结点个数不为0时，从队列取队首元素，并将该元素左右子节点放入队列，下一层结点个数对应增加。
        直到为0时，加到解空间中，并替换为下一层的结点个数开始遍历。
        也可以不记录下一层节点数，因为每一层开始遍历的时候，当前队列的节点数量正好是当前层的节点个数。
        :param root:
        :return:
        """
        if not root:
            return []
        q = [root]
        level = []
        while q:
            cur_level = []
            num = len(q)
            while num:
                node = q.pop(0)
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                num -= 1
            level.append(cur_level)
        return level
        """
        DFS方法也可以做。因为dfs搜索时无视层，所以可以传入一个层数的参数，将所有该层的节点放入层对应list的末尾。
        """
        def dfs(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        if not root:
            return []
        ans = []
        dfs(root, 0)
        return ans
